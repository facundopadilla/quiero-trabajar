from . import db
from uuid import uuid4
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from .users import User

class Employee(User):
    __tablename__ = "employee"

    