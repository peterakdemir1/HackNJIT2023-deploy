import streamlit as st
import base64
import sys
sys.path.append('..')
# from st_pages import Page, show_pages, add_page_title

st.markdown("<h1 style='text-align: center;'>Upload Challenge</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image", type=["png","jpg"])

if uploaded_file is not None:
    # Display the uploaded image as HTML
    # Read the image file as bytes
    image_bytes = uploaded_file.read()
    # Encode the image bytes as base64
    image_base64 = base64.b64encode(image_bytes).decode()
    # st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="Uploaded Image">', unsafe_allow_html=True)


submit_button = st.button("Submit")

# st.write(st.session_state.username)


if submit_button:
    if uploaded_file is not None:
        # convert to Base64
        bytes_data = uploaded_file.getvalue()
        image_base64 = base64.b64encode(bytes_data).decode()
        # st.markdown(result)
        st.markdown(f'<img src="data:image/png;base64,{image_base64}" alt="Uploaded Image" style="width: 200px; height: auto;">', unsafe_allow_html=True)
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
