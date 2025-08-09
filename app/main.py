from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import Optional
import os

from .db import Base, engine, get_db
from . import models, schemas
from .utils import random_slug

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Link Shortener", version="0.1.0")

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

@app.post("/api/urls", response_model=schemas.URLInfo, status_code=201)
def create_url(payload: schemas.URLCreate, db: Session = Depends(get_db)):
    # si custom_slug está ocupado -> 409
    slug: Optional[str] = payload.custom_slug
    if slug:
        existing = db.query(models.URL).filter_by(slug=slug).first()
        if existing:
            raise HTTPException(status_code=409, detail="Slug already in use")
    else:
        # generar hasta encontrar uno libre
        for _ in range(5):
            slug = random_slug()
            if not db.query(models.URL).filter_by(slug=slug).first():
                break
        else:
            raise HTTPException(status_code=500, detail="Could not generate unique slug")

    item = models.URL(original=str(payload.url), slug=slug)
    db.add(item)
    db.commit()
    db.refresh(item)
    return schemas.URLInfo(slug=item.slug, url=item.original, clicks=item.clicks)

@app.get("/api/urls/{slug}", response_model=schemas.URLInfo)
def get_info(slug: str, db: Session = Depends(get_db)):
    item = db.query(models.URL).filter_by(slug=slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return schemas.URLInfo(slug=item.slug, url=item.original, clicks=item.clicks)

@app.delete("/api/urls/{slug}", status_code=204)
def delete_url(slug: str, db: Session = Depends(get_db)):
    item = db.query(models.URL).filter_by(slug=slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(item)
    db.commit()
    return

@app.get("/{slug}")
def redirect(slug: str, db: Session = Depends(get_db)):
    item = db.query(models.URL).filter_by(slug=slug).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    item.clicks += 1
    db.commit()
    # 307 mantiene método; para links es OK 302/307
    return RedirectResponse(item.original, status_code=status.HTTP_307_TEMPORARY_REDIRECT)

@app.get("/healthz")
def healthz():
    return {"status": "ok", "base_url": BASE_URL}
