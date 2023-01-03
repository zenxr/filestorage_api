from database import models
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from services import schemas

async def get_user(db: AsyncSession, user_id: int):
    db_exec = await db.execute(select(models.User).where(models.User.id == user_id))
    return db_exec.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    return await db.execute(select(models.User).where(models.User.email == email))


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    db_exec = await db.execute(select(models.User).offset(skip).limit(limit))
    return db_exec.scalars().all()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
