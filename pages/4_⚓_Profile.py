import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain

p1 = 2
p2 = 5
p3 = 7
p4 = 8
p5 = 2
p6 = 6
p7 = 3

st.markdown("<h1 style='text-align: center;'>Profile</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Logged in as: " + st.session_state.username)
log_out = st.sidebar.button("Log Out")

st.markdown(f'''
<h2>{st.session_state.username} Statistics<h2><h3>Rewards</h3>
<p>🏴‍☠️: {p1} found!</p>
<p>⛵: {p2} found!</p>
<p>❌: {p3} found!</p>
<p>⚓: {p4} found!</p>
<p>🧭: {p5} found!</p>
<p>🌊: {p6} found!</p>
<p>🦜: {p7} found!</p>
<br>

<h3>Uploaded Images</h3>
<p>Put each image here</p>
''', unsafe_allow_html=True)

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