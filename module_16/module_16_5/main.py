from fastapi import FastAPI, status, Body, Path, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user_list": users})


@app.get("/user/{user_id}", response_class=HTMLResponse)
def get_user(request: Request, user_id: int) -> HTMLResponse:
    if user_id < 1 or user_id > len(users):
        raise HTTPException(status_code=404, detail="User not found")

    user = users[user_id - 1]
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post("/user", response_class=HTMLResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: Request, username: str = Form(...), age: int = Form(...)) -> HTMLResponse:
    user_id = len(users) + 1  # Генерация нового ID
    new_user = User(id=user_id, username=username, age=age)  # Создаем нового пользователя
    users.append(new_user)  # Добавляем нового пользователя в список
    return templates.TemplateResponse("users.html", {"request": request, "user_list": users})


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
        raise HTTPException(status_code=404, detail="User {user_id} is not")
