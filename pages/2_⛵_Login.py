import streamlit as st
from dbconfig import users_dao, images_dao
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain



st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)

# establish database connection here

with st.form("Login"):
    user_name = st.text_input('Username')
    user_password = st.text_input('Password', type='password')
    verify_user = st.form_submit_button("Login")

# verify if user exists
if verify_user:
 #    verify(user_name, user_password)
    print("temp")

# for when we establish log in view

# show_pages(
# [
#         # Page("1_🌌_Home.py", "Home", "🌌"),
#         Page("1_🌌_HomeLogIn.py", "Home", "🌌"),
#         # Page("pages/2_👾_Instructions.py", "Instructions", "👾"),
#         Page("pages/2_👾_InstructionsLogIn.py", "Instructions", "👾"),
#         # Page("pages/3_👽_Login.py", "Login", "👽"),
#         Page("pages/4_🎮_Play.py", "Play", "🎮"),
#         # Page("pages/5_🛸_Register.py", "Register", "🛸"),
#         Page("pages/6_⬆️_Upload.py", "Upload", "⬆️"),
#         Page("pages/7_Leaderboard.py", "Leaderboard", "⬆️")
# ])
# sleep(1)