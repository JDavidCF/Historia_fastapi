from fastapi import FastAPI
from routers.historia import router

app = FastAPI()

app.include_router(router)