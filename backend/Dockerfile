FROM python:3.11-slim

WORKDIR /app

# System deps (minimal, helps some libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Env settings (faster + cleaner logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first (better caching)
COPY requirements.txt .

# Install deps (stable for slow networks)
RUN pip install --no-cache-dir \
    --default-timeout=100 \
    --retries=20 \
    --prefer-binary \
    -r requirements.txt

# (OPTIONAL) Only if you REALLY use torch
# RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Copy app
COPY . .

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]