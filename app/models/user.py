from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MinLengthValidator, RegexValidator
from tortoise.contrib.pydantic import pydantic_model_creator
from uuid import uuid4
from re import I as FLAG_IGNORECASE
from .validators import validators

class UserModel(Model):
    id = fields.UUIDField(pk=True, default=uuid4, description="The ID of user")
    date_created = fields.DatetimeField(auto_now_add=True, description="The date of creation")
    first_name = fields.CharField(null=False, description="The first name of the user", max_length=16, validators=[validators.MinAndMaxValidator(3, 16), RegexValidator("[a-zA-Z]", FLAG_IGNORECASE)])
    last_name = fields.CharField(null=False, description="The last name of the user", max_length=20, validators=[validators.MinAndMaxValidator(3, 20), RegexValidator("[a-zA-Z]", FLAG_IGNORECASE)])
    birthday = fields.DatetimeField(auto_now=True, description="The birthday of the user")
    email = fields.CharField(null=False, description="The email of the user", max_length=50, validators=[validators.MinAndMaxValidator(7, 50), validators.EmailValidator()])
    phone_number = fields.CharField(null=True, description="The phone number of the user", max_length=20, validators=[validators.MinAndMaxValidator(6, 20), validators.PhoneValidator()])
    username = fields.CharField(null=False, unique=True, max_length=20, description="Username", validators=[validators.MinAndMaxValidator(3, 20), validators.UsernameValidator()])
    password = fields.CharField(null=False, max_length=20, description="Password", validators=[validators.PasswordValidator()])
    confirm_email = fields.BooleanField(description="True is confirmed, False is not confirmed", default=False)
    country = fields.CharField(null=False, max_length=25, description="The country of the user", validators=[MinLengthValidator(3)])
    city = fields.CharField(null=False, max_length=40, description="The city of the user", validators=[validators.MinAndMaxValidator(3, 40)])
    website = fields.TextField(null=True, description="The website of the user", validators=[validators.WebValidator()])

    def __str__(self):
        return self.username
    
    class Meta:
        table = "users"

User_Pydantic = pydantic_model_creator(UserModel, name="User")
UserIn_Pydantic = pydantic_model_creator(UserModel, name="UserIn", exclude_readonly=True)