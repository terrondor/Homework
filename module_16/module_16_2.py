from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/user/{username}/{id}')
async def get_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]) -> dict:
    return {"message": f"Hello, {user_id}"}


@app.get('/user/{username}/{age}')
async def get_user_age(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> dict:
    return {"message": f"Hello, {username}! Your age is {age}"}
