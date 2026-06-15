from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import SessionLocal

import crud

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/")
def search_settings(
    query: str,
    db: Session = Depends(get_db)
):

    return crud.search_settings(
        db,
        query
    )