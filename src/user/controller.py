from fastapi import HTTPException, status, Request
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError


password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)



def register(body: UserSchema, db: Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()

    if is_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        username=body.username,
        name=body.name,
        email=body.email,
        hash_password=hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def login(body: LoginSchema, db:Session):

    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Invalid username")

    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="Invalid password")


    exp_time = datetime.now() + timedelta(minutes = settings.EXP_TIME)

    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": exp_time
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return {"token": token}


#TOKEN send:-

def is_authenticated(request: Request, db: Session):
    try:
        token = request.headers.get("Authorization")

        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to access this resource")

        token = token.split(" ")[-1]
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        user_id = data.get("user_id")
        
        


        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized")


        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


