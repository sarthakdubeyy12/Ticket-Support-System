from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import models
import auth
import database
from bson import ObjectId

router = APIRouter()

@router.post("/register/")
def register(user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_admin=False
    )
    database.db.users.insert_one(new_user.dict())
    return {"message": "User registered successfully"}

@router.post("/login/")
def login(user: schemas.UserCreate):
    db_user = database.db.users.find_one({"email": user.email})
    if not db_user or not auth.verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = auth.create_access_token(data={"sub": db_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/submit-ticket/")
def submit_ticket(ticket: schemas.TicketCreate, current_user: models.User = Depends(get_current_user)):
    new_ticket = models.Ticket(
        title=ticket.title,
        description=ticket.description,
        category=ticket.category,
        user_id=str(current_user["_id"])
    )
    database.db.tickets.insert_one(new_ticket.dict())
    return {"message": "Ticket submitted successfully"}

@router.get("/tickets/")
def get_tickets(current_user: models.User = Depends(schemas.get_current_user)):
    tickets = database.db.tickets.find({"user_id": str(current_user["_id"])})
    return list(tickets)

def get_current_user(token: str = Depends(schemas.oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = schemas.jwt.decode(token, schemas.SECRET_KEY, algorithms=[schemas.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except schemas.JWTError:
        raise credentials_exception
    user = database.db.users.find_one({"email": token_data.username})
    if user is None:
        raise credentials_exception
    return user