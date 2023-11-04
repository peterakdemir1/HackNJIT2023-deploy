import streamlit as st
from dbconfig import users_dao, images_dao
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain
import time



st.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)

# establish database connection here

with st.form("Login"):
    user_name_email = st.text_input('Username/Email')
    user_password = st.text_input('Password', type='password')
    verify_user = st.form_submit_button("Login")

# verify if user exists
if verify_user:
    user = {'username': user_name_email, 'password': user_password} if '@' not in user_name_email else {'email': user_name_email, 'password': user_password}
    print(user)
    fetchedUserList = users_dao.find_any(user)
    print(fetchedUserList)
    if users_dao.find_any(user):
        st.session_state.username = fetchedUserList[0]['username']
        st.session_state.logged_in = True
        st.success('Successful Login!')
        time.sleep(1)
        switch_page('Play')
    else:
        st.warning('Incorrect Username/Password.')

        
