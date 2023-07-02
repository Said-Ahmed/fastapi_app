from fastapi import FastAPI

from operations.routers import router as router_operations

app = FastAPI()


app.include_router(router_operations)