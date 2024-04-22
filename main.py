from fastapi import FastAPI
from routes.regestration.index import user
from routes.login.index import log
from routes.resources.index import res
app = FastAPI()

app.include_router(user)
app.include_router(log)
app.include_router(res)