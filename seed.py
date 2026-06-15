from database import SessionLocal

from models import (
    Setting,
    ConfigurationGroup
)

db = SessionLocal()

group = ConfigurationGroup(
    name="General",
    description="General Settings"
)

db.add(group)

db.commit()

db.refresh(group)

settings = [

    {
        "keyName":
        "privacy_mode",

        "value":
        "strict",

        "description":
        "Controls privacy options",

        "category":
        "Privacy",

        "systemSetting":
        True,

        "group_id":
        group.id
    },

    {
        "keyName":
        "email_notifications",

        "value":
        "enabled",

        "description":
        "Controls notification emails",

        "category":
        "Notifications",

        "systemSetting":
        False,

        "group_id":
        group.id
    }

]

for item in settings:

    setting = Setting(**item)

    db.add(setting)

db.commit()

print("Database Seeded")