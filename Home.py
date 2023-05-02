import json
import streamlit as st
import streamlit.components.v1 as html
from streamlit_lottie import st_lottie
from styling import (home)

st.set_page_config(
    page_title="Nezaysr",
    page_icon="👹",
)

st.title("Fullstack Developer")
st.write("""
Hello i'm Neza Yasser, welcome to my Streamlit app project \n
""")
with open('static/72233-south-america.json', 'r') as f:
    animation = json.load(f)

# Display the animation
st_lottie(animation, speed=1, width=200, height=200)
st.markdown(home.index(), unsafe_allow_html=True)
