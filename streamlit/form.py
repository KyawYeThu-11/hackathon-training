import streamlit as st

# Form
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

# Data Validation
with st.form("registration"):
    st.write("Inside the form")
    password = st.text_input('Password', placeholder='The password must have at least 8 characters', type="password")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if len(password) < 8:
            st.error('The password is too short.')
        elif not checkbox_val:
            st.error('The checkbox is not checked.')
        else:
            st.snow()
            st.write("password", password, "checkbox", checkbox_val)

st.write("Outside the form")