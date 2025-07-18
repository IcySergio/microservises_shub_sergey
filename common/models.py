from typing import Union, List
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column, Integer, String
from sqlalchemy import Integer, String, Boolean, JSON
from sqlalchemy.orm import Mapped, mapped_column

from common import Base


class Corpus(Base):
    __tablename__ = "corpuses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(JSONB, nullable=False)