# FastAPI dependencies
from fastapi import APIRouter, Depends

# Employee
from ..models.employee import Employee
from ..models.schemas.employee import EmployeeModel

# Job
from ..models.jobs import Job

# OAuth2 Scheme
from ..security.oauth import oauth2_scheme

router = APIRouter()

@router.get("/employee/{uid}", tags=["employee"])
async def get_employee(token: str = Depends(oauth2_scheme), uid: str):
    employee = await Employee.get_or_404(uid)
    jobs = await Job.query.where(Job.employee_id == employee.id).gino.all()
    employee = employee.to_dict()
    employee["jobs"] = [job.to_dict() for job in jobs]
    return employee

@router.post("/employee", tags=["employee"])
async def add_employee(employee: EmployeeModel):
    data = dict(employee)
    r = await Employee.create(**data)
    return data

@router.delete("/employee/{uid}", tags=["employee"])
async def delete_employee(uid: str):
    employee = Employee.get_or_404(uid)
    await employee.delete()
    return {"message": "The user with id '{uid}' deleted successfully"}

def init_app(app):
    app.include_router(router)

