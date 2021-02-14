from fastapi import FastAPI
from models import *
from typing import List
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="QuieroTrabajar API v1")

@app.get("/api/v1/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(UserModel.all())

@app.post("/api/v1/users", response_model=User_Pydantic)
async def post_user(user: UserIn_Pydantic):
    user_obj = await UserModel.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)

register_tortoise(
    app,
    db_url = 'postgres://root:12345678@0.0.0.0:15432/fastapi',
    modules={"models":['models']},
    generate_schemas=True,
    add_exception_handlers=True
)

