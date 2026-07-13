import streamlit as st
import random
import time
import base64

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="wide"
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🎮 Game Settings")

game_mode = st.sidebar.selectbox(
    "Match Type",
    ["Best of 3", "Best of 5", "Best of 7"]
)

music = st.sidebar.toggle("🎵 Background Music", value=True)


if game_mode == "Best of 3":
    target = 2
elif game_mode == "Best of 5":
    target = 3
else:
    target = 4

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#101522,#1B263B);
    color:white;
}

h1,h2,h3,h4{
    text-align:center;
    color:white;
}

div.stButton > button{
    width:100%;
    height:55px;
    border-radius:18px;
    font-size:20px;
    font-weight:bold;
    border:none;
    background:#00A8E8;
    color:white;
    transition:0.3s;
}

div.stButton > button:hover{
    transform:scale(1.05);
    background:#0077B6;
}

.block-container{
    padding-top:2rem;
}

.score{
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.history{
    background:#222;
    border-radius:10px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# BACKGROUND MUSIC
# ----------------------------------------------------

def autoplay_music(file):

    with open(file, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)


if music:
    autoplay_music("assets/background.mp3")

# ----------------------------------------------------
# PLAY SOUND EFFECT
# ----------------------------------------------------

def play_sound(file):

    with open(file, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draw_score" not in st.session_state:
    st.session_state.draw_score = 0

if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------------------------------
# TITLE
# ----------------------------------------------------

st.markdown("""
<h1 style='text-align:center;
color:#FFD700;
font-size:55px;'>
🎮 ROCK • PAPER • SCISSORS
</h1>
""", unsafe_allow_html=True)

st.write("---")

# ----------------------------------------------------
# SCOREBOARD
# ----------------------------------------------------

st.markdown("""
<h2 style='text-align:center;
color:#FFD700;'>
🏆 LIVE SCORE
</h2>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("🙋 You",st.session_state.user_score)

with c2:
    st.metric("🤝 Draw",st.session_state.draw_score)

with c3:
    st.metric("💻 Computer",st.session_state.computer_score)

st.write("---")

# ----------------------------------------------------
# IMAGE PATHS
# ----------------------------------------------------

images={

    "Rock":"assets/rock.png",

    "Paper":"assets/paper.png",

    "Scissors":"assets/scissors.png"

}

# ----------------------------------------------------
# PLAYER CHOICE
# ----------------------------------------------------

st.subheader("Choose Your Move")

col1,col2,col3=st.columns(3)

user_choice=None

IMAGE_SIZE = 80

with col1:
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.image(images["Rock"], width=IMAGE_SIZE)
    if st.button("🪨 ROCK", use_container_width=True):
        user_choice = "Rock"

with col2:
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.image(images["Paper"], width=IMAGE_SIZE)
    if st.button("📄 PAPER", use_container_width=True):
        user_choice = "Paper"

with col3:
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.image(images["Scissors"], width=IMAGE_SIZE)
    if st.button("✂️ SCISSORS", use_container_width=True):
        user_choice = "Scissors"

# ----------------------------------------------------
# COUNTDOWN
# ----------------------------------------------------

if user_choice:

    countdown=st.empty()

    for word in ["🪨 ROCK", "📄 PAPER", "✂️ SCISSORS", "🚀 SHOOT!"]:
        countdown.markdown(
            f"""
            <h1 style='text-align:center;
            color:#FFD700;
            font-size:60px;'>
            {word}
            </h1>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.6)

    countdown.empty()

    computer_choice=random.choice(["Rock","Paper","Scissors"])

    st.write("---")

    left,right=st.columns(2)

    RESULT_IMAGE_SIZE = 120


    with left:
        st.subheader("🙋 You")
        _, center, _ = st.columns([1, 2, 1])
        with center:
            st.image(images[user_choice], width=RESULT_IMAGE_SIZE)

    with right:
        st.subheader("💻 Computer")
        _, center, _ = st.columns([1, 2, 1])
        with center:
            st.image(images[computer_choice], width=RESULT_IMAGE_SIZE)

    # Result Logic will be added in Part 2
    st.write("---")

    # -----------------------------
    # Determine Winner
    # -----------------------------

    if user_choice == computer_choice:

        result = "🤝 Draw"

        st.markdown(
f"""
<div style="
background:#1565C0;
padding:20px;
border-radius:15px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;">
{result}
</div>
""",
unsafe_allow_html=True
)

        st.session_state.draw_score += 1

        play_sound("assets/draw.mp3")


    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):

        result = "🎉 You Win!"

        st.markdown(
f"""
<div style="
background:#0E7C3A;
padding:20px;
border-radius:15px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;">
{result}
</div>
""",
unsafe_allow_html=True
)

        st.balloons()

        st.session_state.user_score += 1

        play_sound("assets/win.mp3")


    else:

        result = "😢 Computer Wins!"

        st.markdown(
f"""
<div style="
background:#B00020;
padding:20px;
border-radius:15px;
text-align:center;
font-size:30px;
font-weight:bold;
color:white;">
{result}
</div>
""",
unsafe_allow_html=True
)

        st.snow()

        st.session_state.computer_score += 1

        play_sound("assets/lose.mp3")


    # -----------------------------
    # Match History
    # -----------------------------

    st.session_state.history.insert(
    0,
    {
        "You": user_choice,
        "Computer": computer_choice,
        "Result": result
    }
    )
    
    if st.session_state.user_score >= target:

        st.success("🏆 Congratulations! You Won The Match!")
        st.balloons()
        
    elif st.session_state.computer_score >= target:

        st.error("💻 Computer Won The Match!")
        st.snow()


st.write("---")

# -----------------------------
# Match History
# -----------------------------

st.subheader("📜 Match History")

if len(st.session_state.history) == 0:

    st.info("No matches played yet.")

else:

    history=[]

    for match in st.session_state.history:

        history.append(
            {
                "You":match["You"],
                "Computer":match["Computer"],
                "Result":match["Result"]
            }
        )

    st.table(history)


st.write("---")


st.subheader("📊 Statistics")

total = (
    st.session_state.user_score
    + st.session_state.computer_score
    + st.session_state.draw_score
)

if total > 0:

    win_rate = st.session_state.user_score / total * 100

    st.progress(int(win_rate))
    st.metric("Winning Percentage", f"{win_rate:.1f}%")

    st.write(f"Win Rate: **{win_rate:.1f}%**")

    st.write(f"Total Games: **{total}**")
    
# -----------------------------
# Reset Button
# -----------------------------

if st.button("🔄 Reset Game"):

    st.session_state.user_score = 0

    st.session_state.computer_score = 0

    st.session_state.draw_score = 0

    st.session_state.history = []

    st.rerun()

st.divider()

st.markdown("""
<div style='text-align:center;
color:gray;
font-size:18px;'>

Made with ❤️ by Sai Mahesh

</div>
""", unsafe_allow_html=True)