# Build stage
FROM python:3.9.6-slim-buster as builder
RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --upgrade pip
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .
ENV PATH="/root/.local/bin:${PATH}"
RUN streamlit version

# Production stage
FROM python:3.9.6-slim-buster
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://code-server.dev/install.sh | sh
EXPOSE 8501
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /app
CMD ["streamlit", "run", "--server.port", "8501", "--server.enableCORS", "false", "Home.py"]
