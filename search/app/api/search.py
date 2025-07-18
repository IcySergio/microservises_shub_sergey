from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from Levenshtein import distance as levenshtein
from common.models import Corpus
from search.dependencies import get_session
from search.schemas import SearchRequest, SearchResponse
from search.app.utils.levenshtein import levenshtein

router = APIRouter(prefix="/search", tags=["search"])

@router.post("/", response_model=SearchResponse)
async def search_corpus(req: SearchRequest, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Corpus.content).where(Corpus.id == req.corpus_id))
    row = result.first()
    if row is None:
        raise HTTPException(status_code=404, detail="Corpus not found")

    content_dict: dict[str, bool] = row[0]
    scored = sorted(content_dict.keys(), key=lambda k: levenshtein(req.text.lower(), k.lower()))
    return SearchResponse(matches=scored[: req.limit])