from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional
from database import get_db
from bson import ObjectId

# This secret key should be kept safe
SECRET_KEY = "e81294f16bda8a1f458c254f97728dbb5c72af0c113fb03b52c92d52c664c499"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: str
    is_active: bool

class UserInDB(User):
    hashed_password: str

# Dependency
def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
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
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = db.users.find_one({"username": token_data.username})
    if user is None:
        raise credentials_exception
    return UserInDB(**user)

# Other Pydantic models for tickets
class TicketCreate(BaseModel):
    title: str
    description: str
    category: str
