import streamlit as st

# side bar
# st.markdown('<h2 style="text-align: center;">Registration Form</h2>', unsafe_allow_html=True)
st.title("This is title.")
st.header("This is header, so it's smaller.")
st.subheader("This is sub-header, so it's even more smaller.")

with st.sidebar:
    st.write('Hello World')

    st.image('images/river.jpg', width=300, caption='Sunrise by the mountains')

st.audio('audio/Never_Gonna_Give_You_Up.mp3')

st.video('https://youtu.be/dQw4w9WgXcQ')

# columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Object Notation
st.sidebar.write('This is a text element on the sidebar but by using object notation.')
col2.caption('This is a dog -- I forgot to put the caption -;-')

# Expander
with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")

# Container
container = st.container()

container.write("This is inside the container")
st.write("This is outside the container")
container.write("This is inside too")

# Empty
## Comment out each from bottom-up
placeholder = st.empty()

placeholder.text("Hello")

placeholder.line_chart({"data": [1, 5, 2, 6]})

with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

placeholder.empty()