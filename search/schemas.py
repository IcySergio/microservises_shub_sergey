from pydantic import BaseModel, Field
from typing import List


class SearchRequest(BaseModel):
    corpus_id: int = Field(..., description="ID корпуса")
    text: str = Field(..., description="Что ищем")
    limit: int = Field(5, ge=1, le=50, description="Сколько результатов вернуть")


class SearchResponse(BaseModel):
    matches: List[str]