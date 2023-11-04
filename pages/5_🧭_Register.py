import streamlit as st

st.markdown("<h1 style='text-align: center;'>Register</h1>", unsafe_allow_html=True)


with st.form("Register"):
	register_username = st.text_input('Username')
	register_password = st.text_input('Password', type='password')
	flag = st.form_submit_button('Register')
	
if flag:
        # verify(register_username, register_password)  
        st.write("registered", register_username)