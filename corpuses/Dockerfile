FROM python:3.12-slim

WORKDIR /app

COPY corpuses/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY corpuses /app/corpuses
COPY common /app/common

ENV PYTHONPATH=/app

CMD ["uvicorn", "corpuses.main:app", "--host", "0.0.0.0", "--port", "8000"]

