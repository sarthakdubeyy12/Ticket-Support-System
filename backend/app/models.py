from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_admin: bool = False

class Ticket(BaseModel):
    title: str
    description: str
    category: str
    status: str = "Open"
    user_id: str