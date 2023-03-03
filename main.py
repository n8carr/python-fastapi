from fastapi import FastAPI

from api import users, courses, sections

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


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
