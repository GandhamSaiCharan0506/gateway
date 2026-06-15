from sqlalchemy.orm import Session

from models import Setting


def get_all_settings(
    db: Session
):

    return db.query(
        Setting
    ).all()


def create_setting(
    db: Session,
    setting
):

    db_setting = Setting(
        **setting.dict()
    )

    db.add(db_setting)

    db.commit()

    db.refresh(db_setting)

    return db_setting


def update_setting(
    db: Session,
    setting_id: int,
    value: str
):

    setting = db.query(
        Setting
    ).filter(
        Setting.id == setting_id
    ).first()

    if setting:

        setting.value = value

        db.commit()

        db.refresh(setting)

    return setting


def search_settings(
    db: Session,
    query: str
):

    settings = db.query(
        Setting
    ).all()

    query = query.lower()

    matched = []

    for setting in settings:

        combined = f"""
        {setting.keyName}
        {setting.description}
        {setting.category}
        """

        if query in combined.lower():

            matched.append(setting)

    return matched