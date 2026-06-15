from pydantic import BaseModel


class SettingBase(BaseModel):

    keyName: str
    value: str
    description: str
    category: str
    systemSetting: bool
    group_id: int


class SettingCreate(SettingBase):
    pass


class SettingUpdate(BaseModel):

    value: str


class SettingResponse(SettingBase):

    id: int

    class Config:
        orm_mode = True