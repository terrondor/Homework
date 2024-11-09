

from fastapi import FastAPI, Path, status, HTTPException
from typing import Annotated

from fastapi.openapi.utils import status_code_ranges
from pydantic import BaseModel
from typing import List


app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(min_length=1, max_length=15, description="Enter user name:")],
                      age: Annotated[int, Path(ge=1, le=100, description="Enter user age:")]) -> str:
    if users:
        user_id = max(users, key=lambda u: u.id).id + 1
    else:
        user_id = 0
    users.append(User(id=user_id, username=username, age=age))
    return f"User {user_id} is created"



@app.put("/user/{user_id}/{username}/{age}")
def update_message(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user name:")],
                         username: Annotated[str, Path(min_length=1, max_length=15, description="Enter user name:")],
                         age: Annotated[int, Path(ge=1, le=100, description="Enter user age:")]) -> str:
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        return f"User {user_id} is updated"
    except HTTPException:
        raise HTTPException(status_code=404, detail="User {user_id} is not")



@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User {user_id} is deleted"
    except HTTPException:
        raise HTTPException(status_code=404, detail="User {user_id} is not"