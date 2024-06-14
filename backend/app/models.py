from sqlmodel import Field, Relationship, SQLModel,DateTime,String,Integer

from datetime import datetime

class CommonBase(SQLModel):
    create_date: datetime = Field(default=datetime.now())
    update_date: datetime = Field(default=datetime.now())
    delete_yn: bool = Field(default=False)

class User(CommonBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    password: str = Field(nullable=False)
    email: str = Field(unique=True, nullable=False)