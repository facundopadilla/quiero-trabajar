from typing import List
from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import ValidationError, OperationalError
from app.models.user import UserModel, User_Pydantic, UserIn_Pydantic

def get404():
    return {404: {"model": HTTPNotFoundError}}

# Create the router of the endpoint
router = APIRouter()

@router.get("/users", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(UserModel.all())

@router.post("/users", response_model=User_Pydantic)
async def post_user(user: UserIn_Pydantic):
    try:
        user_obj = await UserModel.create(**user.dict(exclude_unset=True))
    except ValidationError as v:
        raise HTTPException(status_code=400, detail=f"{v.args[0]}")
    else:
        return await User_Pydantic.from_tortoise_orm(user_obj)

@router.get("/users/{user_id}", response_model=User_Pydantic, responses=get404())
async def get_user(user_id: str):
    try:
        return await User_Pydantic.from_queryset_single(UserModel.get(id=user_id))
    except OperationalError as o:
        raise HTTPException(status_code=404, detail=f"{o.args[0]}")

@router.put("/users/{user_id}", response_model=User_Pydantic, responses=get404())
async def update_user(user_id: str, user: UserIn_Pydantic):
    try:
        await UserModel.filter(id=user_id).update(**user.dict(exclude_unset=True))
        return await User_Pydantic.from_queryset_single(UserModel.get(id=user_id))
    except ValidationError as v:
        raise HTTPException(status_code=400, detail=f"{v.args[0]}")

@router.delete("/users/{user_id}", responses=get404())
async def delete_user(user_id: str):
    try:
        deleted_count = await UserModel.filter(id=user_id).delete()
        if not deleted_count:
            return HTTPException(status_code=404, detail=f"User {user_id} not found")
        return {"message":f"Deleted user {user_id} successfully"}
    except OperationalError as o:
        raise HTTPException(status_code=404, detail=f"{o.args[0]}")
    