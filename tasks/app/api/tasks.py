from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update as sa_update
from starlette.responses import Response

from ..schemas import UpdateItem, PercentageOut
from ..dependencies import get_session
from common.models import Corpus

router = APIRouter(prefix="/tasks", tags=["tasks"])


# ─────────────────────────── 1. Update boolean value ───────────────────────────
@router.put("/", status_code=204)
async def update_item(data: UpdateItem, session: AsyncSession = Depends(get_session)):
    result = await session.execute(
        select(Corpus).where(Corpus.id == data.corpus_id)
    )
    corpus = result.scalar_one_or_none()
    if not corpus:
        raise HTTPException(404, "Corpus not found")
    if data.key not in corpus.content:
        raise HTTPException(404, "Key not in corpus")
    # меняем в Python-словаре
    corpus.content[data.key] = data.value

    # а теперь «принудительно» пишем в базу
    await session.execute(
        sa_update(Corpus)
        .where(Corpus.id == data.corpus_id)
        .values(content=corpus.content)
    )
    await session.commit()


# ──────────────────── 2. Процент true в одном корпусе ───────────────────────────
@router.get("/{corpus_id}/percent", response_model=PercentageOut)
async def corpus_percent(
    corpus_id: int,
    session: AsyncSession = Depends(get_session),
):
    result = await session.execute(select(Corpus.content).where(Corpus.id == corpus_id))
    row = result.first()
    if row is None:
        raise HTTPException(status_code=404, detail="Corpus not found")

    content: dict[str, bool] = row[0]
    if not content:
        percent = 0.0
    else:
        percent = sum(content.values()) / len(content) * 100

    return PercentageOut(percentage=round(percent, 2))


# ───────────────────── 3. Процент true по всем корпусам ─────────────────────────
@router.get("/percent", response_model=PercentageOut)
async def global_percent(
    session: AsyncSession = Depends(get_session),
):
    result = await session.execute(select(Corpus.content))
    rows = result.scalars().all()

    total_items = sum(len(d) for d in rows)
    total_true = sum(sum(d.values()) for d in rows)

    if total_items == 0:
        percent = 0.0
    else:
        percent = total_true / total_items * 100

    return PercentageOut(percentage=round(percent, 2))
