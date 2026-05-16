FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py .


CMD ["python3", "main.py"]