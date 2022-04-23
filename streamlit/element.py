import streamlit as st

# Text Elements
## title, header, subheader
st.title("This is title.")
st.header("This is header, so it's smaller.")
st.subheader("This is sub-header, so it's even more smaller.")

# write
st.write('Hello World')

# Media Elements
st.image('images/river.jpg', width=300, caption='Sunrise by the mountains')

st.audio('audio/Never_Gonna_Give_You_Up.mp3')

st.video('https://youtu.be/dQw4w9WgXcQ')