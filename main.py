from fastapi import FastAPI
from app.routes.user_route import init_routes

app = FastAPI(title="FastAPI Laravel Style Project")

init_routes(app)
