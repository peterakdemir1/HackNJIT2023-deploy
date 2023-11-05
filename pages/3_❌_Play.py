import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain
import functions as fn
import math
from dbconfig import users_dao, images_dao

def dms_to_dd(degrees, minutes, seconds, direction):
    dd = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ['S', 'W']:
        dd *= -1
    return dd

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

st.markdown("<h1 style='text-align: center;'>Play Challenge</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Logged in as: " + st.session_state.username)
log_out = st.sidebar.button("Log Out")        

# TODO: obtain random image, its riddle, and reward from database
image_obj = images_dao.find_any()
target_image = image_obj[0]["image_bytes"]

riddle = image_obj[0]["riddle"]
reward = image_obj[0]["reward"]
target_coords = image_obj[0]["coordinates"]

if st.button("Next"):

    # get new image, riddle, and reward from database, cycle through
    # if image created by user, skip
    image = Image.open('test2.jpg')
    riddle = "riddle2"
    reward = "🟨"

st.markdown('# Find the treasure!')
st.image(target_image)
st.write(target_coords)
st.markdown(f'### Riddle:\n{riddle}')
st.markdown(f'Reward: {reward}')

uploaded_file = st.file_uploader("Found the treasure? Upload an image of it to complete the challenge!", type=["png","jpg"])

if uploaded_file is not None:
    # Display the uploaded image as HTML
    # Read the image file as bytes
    image_bytes = uploaded_file.read()
    # Encode the image bytes as base64
    image_base64 = base64.b64encode(image_bytes).decode()

submit_button = st.button("Submit")

if submit_button:
    if uploaded_file is not None:
        # convert to Base64
        bytes_data = uploaded_file.getvalue()
        image_base64 = base64.b64encode(bytes_data).decode()
        # st.markdown(result)
        st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="Uploaded Image" style="width: 600px; height: auto;">', unsafe_allow_html=True)
        st.write(st.session_state.username)
        gps_info = fn.get_gps_info(image_base64)
        coordinates = fn.get_coords(gps_info)
        similarity = fn.calc_cosine_similarity(fn.extract_features(image_base64), fn.extract_features(base64.b64encode(target_image).decode()))
        st.markdown(f'Similarity: {similarity*100}%')
        st.write(coordinates)
        # insert into mongo
        # image_data = {
        #     "username": st.session_state.username,
        #     "img_bson": bytes_data,
        #     "coordinates": result
        # }

        # try:
        #     images_dao.insert_one(image_data)
        #     st.success(f'Successfully Uploaded: {uploaded_file.name}')
        # except:
        #     st.error(f'Failed Upload: {uploaded_file.name}')

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