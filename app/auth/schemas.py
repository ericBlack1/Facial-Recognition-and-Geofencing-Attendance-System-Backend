from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    student = "student"
    instructor = "instructor"
    admin = "admin"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: UserRole

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    role: UserRole

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[int] = None
    role: Optional[UserRole] = None
