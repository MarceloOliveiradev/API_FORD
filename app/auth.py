from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
from app.database import get_db
from cryptography.fernet import Fernet

import os

SECRET_KEY = "secret_jwt_key" 
FERNET_KEY = "oQyWgCBMmy4RKeYFKeGGFLuP08zvkGslcThy1c9Iv2I="
fernet = Fernet(FERNET_KEY)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: UserCreate):
    # Verifica se o e-mail já existe
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado.")

    # Verifica se o username já existe
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username já cadastrado.")

    # Verifica se o CPF já existe
    if db.query(User).filter(User.cpf == user.cpf).first():
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")

    hashed_pw = get_password_hash(user.password)
    encrypted_cpf = fernet.encrypt(user.cpf.encode()).decode()

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw,
        is_active=True,
        is_admin=False,
        cpf=encrypted_cpf
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can perform this action.")
    return current_user


