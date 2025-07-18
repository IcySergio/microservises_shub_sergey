from fastapi import FastAPI
from search.app.api.search import router as search_router

app = FastAPI(title="Task Name Search Service")
app.include_router(search_router)