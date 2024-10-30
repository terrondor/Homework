from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_all_users() -> list:
    return users


@app.post("/user/{username}/{age}")
def create_user(
        username: str = Path(min_length=1, max_length=15, description="Enter user name:"),
        age: int = Path(ge=1, le=100, description="Enter user age:")) -> User:
    new_id = (users[-1].id + 1) if users else 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
        user_id: int = Path(ge=1, description="Enter user ID:"),
        username: str = Path(min_length=1, max_length=15, description="Enter user name:"),
        age: int = Path(ge=1, le=100, description="Enter user age:")
) -> User:
    if 0 < user_id <= len(users):
        users[user_id - 1].username = username
        users[user_id - 1].age = age
        return users[user_id - 1]
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int) -> User:
    if 0 < user_id <= len(users):
        deleted_user = users.pop(user_id - 1)
        return deleted_user
    else:
        raise HTTPException(status_code=404, detail="User not found")