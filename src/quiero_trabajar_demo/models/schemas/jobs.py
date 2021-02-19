from faker import Faker
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator

f = Faker()

class JobModel(BaseModel):
    
    employee_id: str = f.uuid4()
    initialization_date: datetime = f.date_time_this_decade()
    finish_date: datetime = f.date_time_this_decade()
    currently_working: bool = f.boolean()
    company: str = f.company()
    position: str = f.job()
    freelance: bool = f.boolean()
    description: str = f.text(max_nb_chars=200)