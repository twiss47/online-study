# default image
FROM python:3.11-slim

# folder
WORKDIR /app

# Requirements Copy
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Project Copy
COPY . .

# Server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

