from pydantic import BaseModel, Field

class UpdateItem(BaseModel):
    corpus_id: int
    key: str
    value: bool

class PercentageOut(BaseModel):
    percentage: float = Field(..., description="0‒100 %")