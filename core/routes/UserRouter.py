from fastapi import APIRouter, Depends
from ..models.User import User,UserCreate
from ...utils.database import get_session
from sqlmodel import Session,select
from passlib.context import CryptContext
import bcrypt

router = APIRouter(prefix='/users',tags=['users'])
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

def hash_password(password:str):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes,salt=salt)
    return hashed_password

def verify_password(plain_password:str,hashed_password:str):
    password_byte_enc = plain_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc,hashed_password)



@router.get("/",response_model=list[User])
async def get_users(session: Session = Depends(get_session)):
    try:
        users= session.exec(select(User)).all()
        return [User(name=user.name,email=user.email) for user in users]
    except Exception as err:
        print(err)

@router.post("/",response_model=User)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    try:
        hashed_pass = hash_password(user.password)
        user = User(name=user.name,email=user.email,password=hashed_pass.decode("utf-8"))
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as err:
        print(err)