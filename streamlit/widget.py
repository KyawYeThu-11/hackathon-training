import string
import streamlit as st
from io import StringIO 

# Button
clicked = st.button('Click Here')
st.write(clicked)
if clicked:
     st.write(":smile:")

# if st.button('Click Here'):
#      st.write(":smile:")

# Multi Select
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'],
     help="This multi select widget allows you to choose multiple favorite colors of yours.")

st.write('You selected:', options)

# Text Input
## placeholder, type
password = st.text_input('Password', placeholder='The password must have at least 8 characters', type="password")
st.write('Your password is', password)

# File Uploader
## uploaded_file.lower(), st.image('uploaded_file')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
     if uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
          # st.write('You uploaded an image file.')
          st.image(uploaded_file, width=300, caption='Uploaded File')

     if uploaded_file.name.lower().endswith(('.txt')):
          # st.write('You uploaded a text file.')

          # To read file as bytes:
          bytes_data = uploaded_file.getvalue()
          st.write(bytes_data)

          data = bytes_data.decode("utf-8")
          st.write(data)

          # # To convert to a string based IO:
          # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
          # st.write(stringio)

          # # To read file as string:
          # string_data = stringio.read()
          # st.write(string_data)



# Camera Input
picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)