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

st_lottie(animation, speed=1, width=200, height=200)

st.header("Running Source code in local")

st.code('''
git clone https://github.com/nezaYSR/streamlit-porto.git
''', language='git')

st.code('''
pip install -r requirement.txt
''', language='python')

st.code('''
source .venv/Scripts/activate
''', language='python')

st.code('''
streamlit run Home.py
''', language='python')

st.divider()

st.header("Running with 🐳 Docker")

st.code('''
git clone https://github.com/nezaYSR/streamlit-porto.git
''', language='git')

st.code('''
docker build -t neza_portfolio .
''', language='python')

st.code('''
docker run -p 8501:8501 neza_portfolio
''', language='python')

st.code('''
streamlit run Home.py
''', language='python')

st.caption(
    "_ensure you're in :blue[root directory] before executing all cli command_ 👍")
