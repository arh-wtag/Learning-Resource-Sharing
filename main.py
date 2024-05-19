from fastapi import FastAPI, Response, Request
from routes.regestration.index import user
from routes.login.index import log
from routes.resources.index import res
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, start_http_server
from starlette.middleware import Middleware
from starlette_exporter import PrometheusMiddleware
import http.server
app = FastAPI()

app.include_router(user)
app.include_router(log)
app.include_router(res)
REQUESTS_COUNT = Counter('app_requests_total', 'Total App Request')
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
app.add_middleware(PrometheusMiddleware)
@app.get("/")
async def root():
    METRICS_PORT=8001
    start_http_server(METRICS_PORT)
    REQUESTS_COUNT.inc()
    REQUESTS.inc()
    return {"message": "Hello World"}

@app.get("/metrics")
async def metrics(response: Response):
    metrics_data = generate_latest()
    response.headers["Content-Type"] = CONTENT_TYPE_LATEST
    return Response(content=metrics_data, media_type=CONTENT_TYPE_LATEST)
