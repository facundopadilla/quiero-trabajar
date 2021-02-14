from pydantic import BaseModel, EmailStr, SecretStr
from datetime import datetime
from typing import List

class Job(BaseModel):
    initialization_date: datetime
    finish_date: datetime
    company: str
    position: str
    freelance: bool
    description: str

class User(BaseModel):
    id: str
    date_created: datetime = None
    first_name: str
    last_name: str
    birthday: datetime
    email: EmailStr
    phone_number: int
    username: str
    password: SecretStr
    confirm_email: bool
    country: str
    city: str
    jobs: List[Job]
    website: str

