from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from corpuses.app.db import get_session
from corpuses.app.schemas import CorpusCreate, CorpusRead
from common.models import Corpus

router = APIRouter(prefix="/corpuses", tags=["corpuses"])

# ─────────────────────────────────────────────────────────────── create
@router.post("/", response_model=CorpusRead, status_code=201)
async def create_corpus(
    data: CorpusCreate,
    session: AsyncSession = Depends(get_session),
):
    content: Dict[str, bool] = {key: False for key in data.keys}
    corpus = Corpus(title=data.title, content=content)
    session.add(corpus)
    await session.commit()
    await session.refresh(corpus)
    return corpus

# ─────────────────────────────────────────────────────────────── read
@router.get("/{corpus_id}", response_model=CorpusRead)
async def get_corpus(
    corpus_id: int,
    session: AsyncSession = Depends(get_session),
):
    result = await session.execute(select(Corpus).where(Corpus.id == corpus_id))
    corpus: Corpus | None = result.scalar_one_or_none()
    if corpus is None:
        raise HTTPException(status_code=404, detail="Corpus not found")
    return corpus

# ─────────────────────────────────────────────────────────────── delete
@router.delete("/{corpus_id}", status_code=204)
async def delete_corpus(
    corpus_id: int,
    session: AsyncSession = Depends(get_session),
):
    result = await session.execute(select(Corpus.id).where(Corpus.id == corpus_id))
    if result.scalar_one_or_none() is None:
        raise HTTPException(status_code=404, detail="Corpus not found")
    await session.execute(delete(Corpus).where(Corpus.id == corpus_id))
    await session.commit()