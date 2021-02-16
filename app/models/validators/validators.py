from tortoise.validators import Validator 
from tortoise.exceptions import ValidationError
from re import match

class MinAndMaxValidator(Validator):

    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value: str):
        if value is None:
            raise ValidationError("Value must not be None - check the validators")
        if not self.min_length <= len(value) <= self.max_length:
            raise ValidationError(f"The length of the value '{value}' must be within the following range: {self.min_length} - {self.max_length}")

class UsernameValidator(Validator):

    def __call__(self, value: str):
        if value is None:
            raise ValidationError("Value must not be None - field: username")
        if not match("^[a-zA-Z0-9_.-]+$", value):
            raise ValidationError(f"Value '{value}' is not a valid username")

class PasswordValidator(Validator):

    def __call__(self, value: str):
        if value is None:
            raise ValidationError("Value must not be None - field: password")
        if not match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$", value):
            raise ValidationError(f"Value '{value}' is not a valid password")

class EmailValidator(Validator):

    def __call__(self, value: str):
        if value is None:
            raise ValidationError("Value must not be None - field: email")
        if not match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', value):
            raise ValidationError(f"Value '{value}' is not a valid email")

class PhoneValidator(Validator):

    def __call__(self, value: str):
        if value is None:
            raise ValidationError("Value must not be None - field: phone")
        if not match('[0-9+-]', value):
            raise ValidationError(f"Value '{value}' is not a valid phone number")

class WebValidator(Validator):

    def __call__(self, value: str):
        if value is None:
            raise ValidationError("Value must not be None - field: website")
        if not match(
            r'https?://[^\s<>"]+|www\.[^\s<>"]+',
            value
        ):
            raise ValidationError(f"Value '{value}' is not a valid URL")
    
