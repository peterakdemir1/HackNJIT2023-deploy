import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain
import functions as fn

st.markdown("<h1 style='text-align: center;'>Play Challenge</h1>", unsafe_allow_html=True)
st.sidebar.markdown("Logged in as: " + st.session_state.username)
log_out = st.sidebar.button("Log Out")        

# TODO: obtain random image, its riddle, and reward from database
image = Image.open('test-images/laptop1.jpg')
riddle = "I dwell with knowledge from floor to floor, In a house with many keys but not a single door. I'm tucked away, where minds grow sharp, Behind volumes of wisdom, I await your harp. Silent rows guard my bed, In a labyrinth of learning, I lay my head. To find me, you must reach higher ground, Where echoes of thought are often found. Climb the stairs, but not too fast, Past wooden sentries, you shall pass. In the heart of tales and tomes, take a look, For I lie hidden in a literary nook."
reward = "🟥"
target_coords = {'latitude': 'longitude'}

if st.button("Next"):

    # get new image, riddle, and reward from database, cycle through
    # if image created by user, skip
    image = Image.open('test2.jpg')
    riddle = "riddle2"
    reward = "🟨"

st.markdown('# Find the treasure!')
st.image(image)
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
        similarity = fn.calc_cosine_similarity(fn.extract_features(image_base64), fn.extract_features())
        st.markdown(f'Similarity: {similarity}')
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