import conf
from sqlalchemy.ext import declarative
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

Base = declarative.declarative_base()


engine = create_async_engine(conf.AppConfig.from_env().database_uri)

async def start_db(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def stop_db(engine: AsyncEngine):
    await engine.dispose()

async def get_session(engine: AsyncEngine):
    session = AsyncSession(engine, expire_on_commit=True)
    try:
        yield session
    finally:
        await session.close()
