# tasks/Dockerfile
FROM python:3.12-slim
WORKDIR /app

COPY tasks/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tasks /app/tasks
COPY common /app/common

CMD ["uvicorn", "tasks.main:app", "--host", "0.0.0.0", "--port", "8000"]