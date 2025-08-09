from sqlalchemy import Column, Integer, String, DateTime, func
from .db import Base

class URL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    original = Column(String(2048), nullable=False)
    slug = Column(String(32), unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
