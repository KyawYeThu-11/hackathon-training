import streamlit as st
import pandas as pd
import csv

# Page configuration
PAGE_CONFIG = {"page_title":"My Map","page_icon":"images/TPH_Icon.png","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():
    with st.form("my_form", clear_on_submit=True):
        st.header("Add a target")
        name = st.text_input('name')
        latitude = st.number_input('latitude', min_value=-90, max_value=90, value=0)
        longitude = st.number_input('latitude', min_value=-180, max_value=180, value=0)

        submitted = st.form_submit_button("Submit")
        if submitted:
            with open('database.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([name, latitude, longitude])

    df = pd.read_csv('database.csv')

    st.table(df)
    st.map(df)

    if st.button('clear'):
        with open('database.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'latitude', 'longitude'])
            st.experimental_rerun()

main()
        