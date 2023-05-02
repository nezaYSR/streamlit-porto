import json
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Nezaysr",
    page_icon="👹",
)

with open('static/51633-run-rex.json', 'r') as f:
    animation = json.load(f)

# Display the animation
st_lottie(animation, speed=1, width=200, height=200)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
