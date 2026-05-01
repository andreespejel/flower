# Python runtime
FROM python:3.11-slim

# System dependencies for PostgreSQL
RUN apt-get update && apt-get install -y \
    # headers for postgres
    libpq-dev \
    # gcc for psycopg2
    gcc \
    # cleanup
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]