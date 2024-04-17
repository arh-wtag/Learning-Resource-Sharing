from fastapi import FastAPI
from routes.regestration.index import user

app = FastAPI()

app.include_router(user)
