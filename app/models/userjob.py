from tortoise import fields
from tortoise.validators import MinLengthValidator
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from uuid import uuid4

class UserJobModel(Model):
    id = fields.UUIDField(default=uuid4, unique=True, null=False, pk=True)
    initialization_date = fields.DatetimeField(auto_now=True, null=False, description="Initialize job")
    finish_date = fields.DatetimeField(auto_now=True, null=False, description="Finish job")
    company = fields.CharField(max_length=100, null=False, description="The name of the company where you worked", validators=[MinLengthValidator(3)])
    position = fields.CharField(max_length=100, null=False, description="What you doing?", validators=[MinLengthValidator(3)])
    freelance = fields.BooleanField(null=False, default=False, description="Do you a worked how freelancer?")
    description = fields.TextField(null=True)

    def __str__(self):
        return self.company
    
    class Meta:
        table = "users_job"

UserJob_Pydantic = pydantic_model_creator(UserJobModel, name="UserJob")
UserJobIn_Pydantic = pydantic_model_creator(UserJobModel, name="UserJobIn", exclude_readonly=True)