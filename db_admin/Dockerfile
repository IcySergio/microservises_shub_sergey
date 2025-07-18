FROM python:3.12-slim
WORKDIR /app

COPY db_admin/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY db_admin/alembic.ini .
COPY db_admin/alembic ./alembic

COPY common ./common
COPY db_admin/entrypoint.sh .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
