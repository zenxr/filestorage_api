from fastapi import FastAPI

from database import base as database
from api import files

database.Base.create_all(database.engine)

app = FastAPI(
    openapi_url="/api/v1/filestorage/openapi.json", docs_url="/api/v1/filestorage/docs"
)


app.include_router(files.router, prefix="/api/v1/filestorage", tags=["filestorage"])
