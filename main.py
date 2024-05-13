from fastapi import FastAPI, Response
from routes.regestration.index import user
from routes.login.index import log
from routes.resources.index import res
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
app = FastAPI()

app.include_router(user)
app.include_router(log)
app.include_router(res)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/metrics")
async def metrics(response: Response):
    metrics_data = generate_latest()
    response.headers["Content-Type"] = CONTENT_TYPE_LATEST
    return Response(content=metrics_data, media_type=CONTENT_TYPE_LATEST)
