from api import files, user
from database import base as database
from fastapi import FastAPI

database.Base.create_all(database.engine)

app = FastAPI(
    openapi_url="/api/v1/filestorage/openapi.json", docs_url="/api/v1/filestorage/docs"
)


@app.on_event("startup")
async def start_db():
    await database.start_db(database.engine)


@app.on_event("shutdown")
async def stop_db():
    await database.stop_db(database.engine)


app.include_router(files.router, prefix="/api/v1/filestorage", tags=["filestorage"])
app.include_router(user.router, prefix="/api/v1/user", tags=["user"])
