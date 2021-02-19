from . import db
from uuid import uuid4
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(UUID(), primary_key=True, unique=True, index=True, nullable=False, default=uuid4)
    employee_id = db.Column('employee_id', None, db.ForeignKey('employee.id'))
    initialization_date = db.Column(db.DateTime, nullable=True)
    finish_date = db.Column(db.DateTime, nullable=True)
    currently_working = db.Column(db.Boolean, nullable=True, default=False)
    company = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    freelance = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text, nullable=True)