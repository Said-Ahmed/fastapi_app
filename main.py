from fastapi import FastAPI

from src.operations.routers import router as router_operations

app = FastAPI()


app.include_router(router_operations)