import streamlit as st

user = "shekhmus" # this will change depending on session
p1 = 2
p2 = 5
p3 = 7
p4 = 8
p5 = 2
p6 = 6
p7 = 3

st.markdown("<h1 style='text-align: center;'>Profile</h1>", unsafe_allow_html=True)

st.markdown(f'''
<h2>{user} Statistics<h2><h3>Rewards</h3>
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
