from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, users
from starlette.staticfiles import StaticFiles
from starlette import status
from fastapi.responses import RedirectResponse


# Subido a rtoutain@vates.com github account
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
