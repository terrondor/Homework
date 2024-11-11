from app.backend.db import engine, Base
from app.models import User, Task
from sqlalchemy.schema import CreateTable


Base.metadata.create_all(bind=engine)


print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))