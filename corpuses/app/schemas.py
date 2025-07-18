from typing import Dict, List
from pydantic import BaseModel

class CorpusCreate(BaseModel):
    title: str
    keys: List[str]

class CorpusRead(BaseModel):
    id: int
    title: str
    content: Dict[str, bool]

    class Config:
        from_attributes = True