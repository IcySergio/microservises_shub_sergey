from fastapi import FastAPI
from corpuses.app.api import corpuses as corpuses_router

app = FastAPI(title="Task Upload Service")
app.include_router(corpuses_router.router)
