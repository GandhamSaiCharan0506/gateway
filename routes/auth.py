from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter(
    prefix="/auth"
)

SPRING_URL = "http://127.0.0.1:8080"

class LoginSchema(BaseModel):

    email: str
    password: str

class RegisterSchema(BaseModel):

    username: str
    email: str
    password: str

@router.post("/login")
async def login(data: LoginSchema):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{SPRING_URL}/auth/login",
            json=data.dict()
        )

        return response.json()

@router.post("/register")
async def register(data: RegisterSchema):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{SPRING_URL}/auth/register",
            json=data.dict()
        )

        return response.json()