# Running local server

git clone https://github.com/nezaYSR/streamlit-porto.git
Go to root directory <br>
pip install -r requirement.txt <br>
source .venv/Scripts/activate <br>
streamlit run Home.py

## Dockerfile

git clone https://github.com/nezaYSR/streamlit-porto.git
Go to root directory <br>
docker build -t neza_portfolio . <br>
docker run -p 8501:8501 neza_portfolio <br>
