import json
import webbrowser
import streamlit as st
import streamlit.components.v1 as html
from streamlit_lottie import st_lottie
from styling import (home)

st.set_page_config(
    page_title="Nezaysr",
    page_icon="👹",
)
with open('static/82423-developer-yoga.json', 'r') as f:
    animation = json.load(f)

st_lottie(animation, speed=1, width=350, height=350)


st.write("""
Hello, I'm Neza Yasser. Welcome to my Streamlit fun project! \n

This project is for demonstration purposes only, so no one will get hurt if something goes wrong. 🙂 \n

If this project were serious, I might use a single Streamlit application and microservices using 
Golang and React for the frontend. Then, I could fetch the Streamlit app using the iframe tag.
""")

st.caption("You can contact/see me through")

if st.button("Github"):
    webbrowser.open_new_tab("https://github.com/nezaYSR")

if st.button("Linkedin"):
    webbrowser.open_new_tab("https://www.linkedin.com/in/nezayasser/")

if st.button("Personal site"):
    webbrowser.open_new_tab("https://nezaysr.tech/")

st.markdown(home.index(), unsafe_allow_html=True)

st.caption("📱Phone: 0813 9850 7029")
st.caption("📧Mail: nezaysr@gmail.com")
