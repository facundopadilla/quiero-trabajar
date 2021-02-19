from fastapi import APIRouter
from ..models.jobs import Job
from ..models.schemas.jobs import JobModel

router = APIRouter()

@router.get("/job/{uid}", tags=["job"])
async def get_job(uid: str):
    job = await Job.get_or_404(uid)
    return job.to_dict()

@router.post("/job", tags=["job"])
async def add_job(job: JobModel):
    data = dict(job)
    r = await Job.create(**data)
    return data

@router.delete("/job/{uid}", tags=["job"])
async def delete_job(uid: str):
    job = Job.get_or_404(uid)
    await job.delete()
    return {"message": "The job with id '{uid}' deleted successfully"}

def init_app(app):
    app.include_router(router)

