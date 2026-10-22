
from fastapi import FastAPI
from routes.health import router as router_health
from routes.check import router as router_check
# from routes.batch import router as router_batch

app = FastAPI()

app.include_router(router_health)
app.include_router(router_check)
# app.include_router(router_batch)