from faker import Faker
from pydantic import BaseModel, ValidationError, validator
from datetime import datetime
from re import fullmatch, match
from urllib.parse import urlparse

f = Faker()

class UserModel(BaseModel):
    first_name: str = f.first_name()
    last_name: str = f.last_name()
    birthday: datetime = f.date_time_this_decade()
    email: str = f.email()
    phone_number: str = f.phone_number()
    username: str = f.simple_profile()["username"]
    password: str = f.password()
    country: str = f.country()
    city: str = f.city()
    website: str = f.profile()["website"][0]

    @validator('first_name')
    def validate_first_name(cls, first_name: str) -> str:
        if 3 <= len(first_name) <= 16:
            if match("[a-zA-Z]", first_name):
                return first_name
            raise ValueError("The 'first_name' field not is valid")
        raise ValueError("The 'first_name' field must be between 3 and 16 characters.")

    @validator('last_name')
    def validate_last_name(cls, last_name: str) -> str:
        if 3 <= len(last_name) <= 16:
            if match("[a-zA-Z]", last_name):
                return last_name
            raise ValueError("The 'last_name' field not is valid")
        raise ValueError("The 'last_name' field must be between 3 and 16 characters.")

    @validator('email')
    def validate_email(cls, email: str) -> str:
        if 7 <= len(email) <= 50:
            if match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$", email):
                return email
            raise ValueError("The 'email' field not is valid")
        raise ValueError("The 'email' field must be between 7 and 50 characters.")

    @validator('phone_number')
    def validate_phone_number(cls, phone_number: str) -> str:
        if 7 <= len(phone_number) <= 20:
            if match("^[-+]?[0-9]+$", phone_number):
                return phone_number
            raise ValueError("The 'phone_number' field not is valid")
        raise ValueError("The 'phone_number' field must between 7 and 20 characters.")

    @validator('username')
    def validate_username(cls, username: str) -> str:
        if 7 <= len(username) <= 20:
            if match("^[a-zA-Z0-9_.-]+$", username):
                return username
            raise ValueError("The 'phone_number' field not is valid")
        raise ValueError("The 'phone_number' field must between 7 and 20 characters.")

    @validator('country')
    def validate_country(cls, country: str) -> str:
        if 3 <= len(country) <= 25:
            if fullmatch(r"^[a-zA-Z\s]+$|^[a-zA-Z]+$", country):
                return country
            raise ValueError("The 'country' field not is valid")
        raise ValueError("The 'country' field must between 3 and 25 characters.")
    
    @validator('city')
    def validate_city(cls, city: str) -> str:
        if 3 <= len(city) <= 40:
            if fullmatch(r"^[a-zA-Z\s]+$|^[a-zA-Z]+$", city):
                return city
            raise ValueError("The 'city' field not is valid")
        raise ValueError("The 'city' field must between 3 and 40 characters.")
    
    @validator('website')
    def validate_website(cls, website: str) -> str:
        if bool(urlparse(website).scheme):
            return website
        raise ValueError("The 'website' field not is valid")


