from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, Возраст:18'}


@app.get("/users")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=1, max_length=15, description="Enter user name:")],
                      age: Annotated[int, Path(ge=1, le=100, description="Enter user age:")]) -> str:
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f'Имя {username}, Возраст: {age}'
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user name:")],
                         username: Annotated[str, Path(min_length=1, max_length=15, description="Enter user name:")],
                         age: Annotated[int, Path(ge=1, le=100, description="Enter user age:")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    if user_id in users:
        return f"User {user_id} is updated"
    else:
        return f"The user {user_id} is registered"


@app.delete("/user/{user_id}")
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} is deleted"