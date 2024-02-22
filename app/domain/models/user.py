from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str
    last_name: str
    cellphone: str = Field(..., unique=True)
    email: EmailStr = Field(..., unique=True)
    password: str
    activation_token: str = ""
    verified_at: datetime = None
