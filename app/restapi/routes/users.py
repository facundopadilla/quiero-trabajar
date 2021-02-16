from typing import List
from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
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
    user_obj = await UserModel.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)

@router.get("/users/{user_id}", response_model=User_Pydantic, responses=get404())
async def get_user(user_id: str):
    return await User_Pydantic.from_queryset_single(UserModel.get(id=user_id))

@router.put("/users/{user_id}", response_model=User_Pydantic, responses=get404())
async def update_user(user_id: str, user: UserIn_Pydantic):
    await UserModel.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(UserModel.get(id=user_id))

@router.delete("/users/{user_id}", responses=get404())
async def delete_user(user_id: str):
    deleted_count = await UserModel.filter(id=user_id).delete()
    if not deleted_count:
        return HTTPException(status_code=404, detail=f"User {user_id} not found")
    return {"message":f"Deleted user {user_id} successfully"}
    