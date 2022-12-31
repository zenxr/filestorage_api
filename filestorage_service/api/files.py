import fastapi
from fastapi import responses
import os

router = fastapi.APIRouter()


@router.get("/add")
async def upload_file(file: fastapi.UploadFile = fastapi.File(...)):
    with open(file.filename, "wb") as f:
        content = await file.read()
        f.write(content)
    return responses.JSONResponse(content={"filename": file.filename}, status_code=200)


@router.get("/get/{filename}")
async def download_file(filename: str):
    return responses.FileResponse(path=f"{os.getcwd()}\\{filename}")


@router.delete("/delete/{}")
async def delete_file(filename: str):
    try:
        os.remove(f"{os.getcwd()}\\{filename}")
    except FileNotFoundError:
        return responses.JSONResponse(
            content={"removed": False, "error_message": "File not found"},
            status_code=404,
        )
    return responses.JSONResponse(content={"removed": True}, status_code=200)


# TODO
# authentication
# route parameters should include bucket name and path
# CRUD on file table, bucket, etc
