FROM python:3.12-slim
WORKDIR /app

COPY search/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY search /app/search

COPY common /app/common

CMD ["uvicorn", "search.main:app", "--host", "0.0.0.0", "--port", "8000"]
