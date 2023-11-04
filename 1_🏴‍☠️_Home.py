import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
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
else:
    show_pages (
        [
            Page("1_🏴‍☠️_Home.py", "Home", "🏴‍☠️"),
            # Page("pages/2_⛵_Login.py", "Login", "⛵"),
            Page("pages/3_❌_Play.py", "Play", "❌"),
            Page("pages/4_⚓_Profile.py", "Profile", "⚓"),
            # Page("pages/5_🧭_Register.py", "Register", "🧭"),
            Page("pages/6_🌊_Upload.py", "Upload", "🌊")
        ]
    )


rain(
    emoji="🌊",
    font_size=54,
    falling_speed=8,
    animation_length="infinite",
)


st.markdown("<h1 style='text-align: center;'>TITLE</h1>", unsafe_allow_html=True)

st.markdown('''
Argh Matey! Explore the world to find me hidden treasures.

Sail to locations in user-uploaded images and collect the 7 treasures of the seven seas

Scan the locations and upload an image to collect me treasure!
''')

if st.button("Login"):
    switch_page('login')

if st.button("Register"):
    switch_page('register')

# col1, col2 = st.columns(2)
# if col1.button("Login"):
#     switch_page("Login")
# if col2.button("Register"):
#     switch_page("Register")