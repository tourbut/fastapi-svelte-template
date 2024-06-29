from app.models import *
from sqlmodel import SQLModel
from sqlmodel import Session, select

class UserCreate(CommonBase):
    username: str
    password1: str
    password2: str
    email: str
    
    @classmethod
    def check_password(self):
        if self.password1 != self.password2:
            return False
        return True

class UserPublic(SQLModel):
    id: int