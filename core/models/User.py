from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    name: str
    email: str
    password: str
    

class User(UserBase, table=True):
    __table_args__ = {"schema": "manager"}
    id: int | None = Field(default=None,primary_key=True,nullable=False)
    

class UserCreate(UserBase):
    pass