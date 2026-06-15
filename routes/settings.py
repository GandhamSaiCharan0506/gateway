from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database import SessionLocal

import crud
import schemas

router = APIRouter(
    prefix="/settings",
    tags=["Settings"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/")
def get_settings(
    db: Session = Depends(get_db)
):

    return crud.get_all_settings(db)


@router.post("/")
def create_setting(
    setting: schemas.SettingCreate,
    db: Session = Depends(get_db)
):

    return crud.create_setting(
        db,
        setting
    )


@router.put("/{setting_id}")
def update_setting(
    setting_id: int,
    setting: schemas.SettingUpdate,
    db: Session = Depends(get_db)
):

    return crud.update_setting(
        db,
        setting_id,
        setting.value
    )