from fastapi import APIRouter
from ..models.users import User
from ..models.schemas.user import UserModel

router = APIRouter()

@router.get("/users/{uid}")
async def get_user(uid: int):
    user = await User.get_or_404(uid)
    return user.to_dict()

@router.post("/users")
async def add_user(user: UserModel):
    rv = await User.create(nickname=user.name)
    return rv.to_dict()

@router.delete("/users/{uid}")
async def delete_user(uid: int):
    user = await User.get_or_404(uid)
    await user.delete()
    return dict(id=uid)

def init_app(app):
    app.include_router(router)