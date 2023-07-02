from fastapi import FastAPI

from database import create_db_and_tables
from operations.routers import router as router_operations

app = FastAPI()


app.include_router(router_operations)