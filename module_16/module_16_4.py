from fastapi import FastAPI, Path, HTTPException
from fastapi import status
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=List[User])
def get_all_users() -> List[User]:
    return users


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(username: str, age: int) -> User:
    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, username: str, age: int) -> User:
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User not found")

    edit_user = users[user_id - 1]
    edit_user.username = username
    edit_user.age = age
    return edit_user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User not found")

    users.pop(user_id - 1)
    return
