FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

# install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# download ReDoc locally
RUN mkdir -p /app/static && \
    curl -o /app/static/redoc.standalone.js \
    https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]