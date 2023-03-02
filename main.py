from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI(
    title="FastAPI Tutorial",
    description="FastAPI Tutorial",
    version="1.0.1",
    contact={
        "name": "Nate Carr",
        "email": "natecarr78@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)


users = []


class User(BaseModel):
    name: str
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(
        id: int = Path(..., description="The ID of the user to retrieve."),
        q: str = Query(None, max_length=5)
):
    return {"user": users[id], "query": q}
