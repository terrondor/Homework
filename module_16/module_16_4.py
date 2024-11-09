from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel



app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_all_users() -> list[User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
def create_user(
        username: str = Path(min_length=1, max_length=15, description="Enter user name:"),
        age: int = Path(ge=1, le=100, description="Enter user age:")) -> User:
    new_id = (users[-1].id + 1) if users else 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}", response_model=User)
def update_user(
        user_id: int = Path(ge=1, description="Enter user ID:"),
        username: str = Path(min_length=1, max_length=15, description="Enter user name:"),
        age: int = Path(ge=1, le=100, description="Enter user age:")
) -> User:
    user = next((u for u in users if u.id == user_id), None)
    if user is not None:
        user.username = username
        user.age = age
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int) -> User:
    user = next((u for u in users if u.id == user_id), None)
    if user is not None:
        users.remove(user)
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")