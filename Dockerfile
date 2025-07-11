FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app
EXPOSE 8502
CMD ["streamlit", "run", "app/main.py", "--server.port=8502", "--server.address=0.0.0.0"]
