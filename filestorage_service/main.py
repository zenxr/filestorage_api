from fastapi import FastAPI

import database
import api

database.metadata.create_all(database.engine)

app = FastAPI(
    openapi_url="/api/v1/filestorage/openapi.json", docs_url="/api/v1/filestorage/docs"
)


@app.on_event("startup")
async def startup():
    await database.get().connect()


@app.on_event("shutdown")
async def shutdown():
    await database.get().disconnect()


app.include_router(api.router, prefix="/api/v1/filestorage", tags=["filestorage"])
