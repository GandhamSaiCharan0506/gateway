from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter(
    prefix="/auth"
)

SPRING_URL = "https://spring-han7.onrender.com"

class LoginSchema(BaseModel):

    email: str
    password: str

class RegisterSchema(BaseModel):

    username: str
    email: str
    password: str

from fastapi import HTTPException

@router.post("/login")
async def login(data: LoginSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SPRING_URL}/auth/login",
            json=data.dict()
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    return response.json()
@router.post("/register")
async def register(data: RegisterSchema):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SPRING_URL}/auth/register",
            json=data.dict()
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    return response.json()