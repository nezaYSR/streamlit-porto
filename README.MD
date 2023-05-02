# Running local server

git clone https://github.com/nezaYSR/streamlit-porto.git
Go to root directory
pip install -r requirement.txt
source .venv/Scripts/activate
streamlit run Home.py

## Dockerfile

git clone https://github.com/nezaYSR/streamlit-porto.git
Go to root directory
docker build -t neza_portfolio .
docker run -p 8501:8501 neza_portfolio
