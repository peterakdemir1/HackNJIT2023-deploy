import streamlit as st
import base64
import sys
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.switch_page_button import switch_page
from functions import *
import io
from dbconfig import *
sys.path.append('..')


st.markdown("<h1 style='text-align: center;'>Upload Challenge</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Logged in as: " + st.session_state.username)
log_out = st.sidebar.button("Log Out")


uploaded_file = st.file_uploader("Choose an image", type=["png","jpg"])

if uploaded_file is not None:
    # Display the uploaded image as HTML
    # Read the image file as bytes
    image_bytes = uploaded_file.read()
    # Encode the image bytes as base64
    image_base64 = base64.b64encode(image_bytes).decode()

submit_button = st.button("Submit")

if submit_button:
    if uploaded_file is not None:

        # st.markdown(result)
        st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="Uploaded Image" style="width: 600px; height: auto;">', unsafe_allow_html=True)
        # st.write(st.session_state.username)
        # print(get_gps_info(image_base64))
        gps_info = get_gps_info(image_base64)
        coordinates = get_coords(gps_info)

        st.write(f"Coordinates: {coordinates}")

        # insert into mongo
        image_data = {
            "username": st.session_state.username,
            "image_bytes": image_bytes,
            "riddle": "test",
            "reward": "test",
            "coordinates": coordinates
        }

        try:
            images_dao.insert_one(image_data)
            st.success(f'Successfully Uploaded: {uploaded_file.name}')
        except:
            st.error(f'Failed Upload: {uploaded_file.name}')

    else:
        st.warning("Please upload a file before submitting.")

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