import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
# from streamlit_extras.let_it_rain import rain
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.let_it_rain import rain

st.markdown("<h1 style='text-align: center;'>Play Challenge</h1>", unsafe_allow_html=True)

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
