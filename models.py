from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    email = Column(
        String,
        unique=True
    )


class ConfigurationGroup(Base):

    __tablename__ = "configuration_groups"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    description = Column(String)


class Setting(Base):

    __tablename__ = "settings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    keyName = Column(
        String,
        unique=True
    )

    value = Column(String)

    description = Column(String)

    category = Column(String)

    systemSetting = Column(
        Boolean,
        default=False
    )

    group_id = Column(
        Integer,
        ForeignKey(
            "configuration_groups.id"
        )
    )

    group = relationship(
        "ConfigurationGroup"
    )