from . import db
from re import match, fullmatch
from uuid import uuid4
from datetime import datetime
from urllib.parse import urlparse
from sqlalchemy.orm import validates
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(), primary_key=True, unique=True, index=True, nullable=False, default=uuid4)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    confirm_email = db.Column(db.Boolean(), default=False)
    country = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    website = db.Column(db.String(120), nullable=True)




