import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain

st.markdown("<h1 style='text-align: center;'>Play Challenge</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Logged in as: " + st.session_state.username)
log_out = st.sidebar.button("Log Out")        

image = Image.open('test1.jpg')
riddle = "riddle1"
reward = "🟥"



if st.button("Next"):

    # get new image, riddle, and reward from database, cycle through
    # if image created by user, skip
    image = Image.open('test2.jpg')
    riddle = "riddle2"
    reward = "🟨"

st.image(image)
st.markdown(riddle)
st.markdown("Reward: ")
st.markdown(reward)

if log_out:
    st.session_state.logged_in = False
    st.session_state.username = None
    show_pages (
        [
            Page("1_🏴‍☠️_Home.py", "Home", "🏴‍☠️"),
            Page("pages/2_⛵_Login.py", "Login", "⛵"),
            # Page("pages/3_❌_Play.py", "Play", "❌"),
            # Page("pages/4_⚓_Profile.py", "Profile", "⚓"),
            Page("pages/5_🧭_Register.py", "Register", "🧭"),
            # Page("pages/6_🌊_Upload.py", "Upload", "🌊")
        ]
    )
    switch_page("Home")