from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class UserCreate(CommonBase):
    username: str
    password: str
    email: EmailStr | None = Field(default=None, max_length=255)

class UserPublic(SQLModel):
    id: int