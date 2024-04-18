from fastapi import FastAPI
from routes.regestration.index import user
from routes.login.index import log

app = FastAPI()

app.include_router(user)
app.include_router(log)