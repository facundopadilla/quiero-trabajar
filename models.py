from tortoise import fields
from tortoise.validators import MinLengthValidator
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from uuid import uuid4

class UserJobModel(Model):
    id = fields.UUIDField(default=uuid4, unique=True, null=False, pk=True)
    initialization_date = fields.DatetimeField(auto_now=True, null=False, description="Initialize job")
    finish_date = fields.DatetimeField(auto_now=True, null=False, description="Finish job")
    company = fields.CharField(max_length=100, null=False, description="The name of the company where you worked")
    position = fields.CharField(max_length=100, null=False, description="What you doing?")
    freelance = fields.BooleanField(null=False, default=False, description="Do you a worked how freelancer?")
    description = fields.TextField(null=True)

    def __str__(self):
        return self.company
    
    class Meta:
        table = "user_job"

class UserModel(Model):
    id = fields.UUIDField(pk=True, default=uuid4, description="The ID of user")
    date_created = fields.DatetimeField(auto_now_add=True, description="The date of creation")
    first_name = fields.CharField(null=False, description="The first name of the user", max_length=16, validators=[MinLengthValidator(3)])
    last_name = fields.CharField(null=False, description="The last name of the user", max_length=20, validators=[MinLengthValidator(3)])
    birthday = fields.DatetimeField(auto_now=True, description="The birthday of the user")
    email = fields.CharField(null=False, description="The email of the user", max_length=120, validators=[MinLengthValidator(7)])
    phone_number = fields.CharField(null=True, description="The phone number of the user", max_length=20, validators=[MinLengthValidator(6)])
    username = fields.CharField(null=False, unique=True, max_length=20, description="Username", validators=[MinLengthValidator(3)])
    password = fields.CharField(null=False, max_length=128, description="Password", validators=[MinLengthValidator(8)])
    confirm_email = fields.BooleanField(description="True is confirmed, False is not confirmed", default=False)
    country = fields.CharField(null=False, max_length=25, description="The country of the user", validators=[MinLengthValidator(3)])
    city = fields.CharField(null=False, max_length=40, description="The city of the user", validators=[MinLengthValidator(3)])
    jobs = fields.ForeignKeyField("models.UserJobModel", related_name="jobs", on_delete=fields.CASCADE)
    website = fields.TextField(null=True, description="The website of the user", validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.username
    
    class Meta:
        table = "user"

User_Pydantic = pydantic_model_creator(UserModel, name="User")
UserIn_Pydantic = pydantic_model_creator(UserModel, name="UserIn", exclude_readonly=True)
UserJob_Pydantic = pydantic_model_creator(UserJobModel, name="UserJob")
UserJobIn_Pydantic = pydantic_model_creator(UserJobModel, name="UserJobIn", exclude_readonly=True)

"""class UserJob(BaseModel):
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
"""