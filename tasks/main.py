from fastapi import FastAPI
from tasks.app.api.tasks import router as tasks_router

app = FastAPI(title="Task‑Manager Service")
app.include_router(tasks_router)