import fastapi
from database import base as database
from fastapi import HTTPException, responses
from services import user
from sqlalchemy.ext.asyncio import AsyncSession

router = fastapi.APIRouter()


@router.get("{user_id}")
async def get_user(
    user_id: int, db: AsyncSession = fastapi.Depends(database.get_session)
) -> responses.Response:
    db_user = await user.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# TODO
# user enrollment, salt password, allow signup
#  - future enhancement: toggle signup allowed
# CRUD on users with authentication
