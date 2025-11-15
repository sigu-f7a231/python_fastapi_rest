from fastapi import FastAPI
from app.crud.user.route import router as user_router

def create_app() -> FastAPI:
    app = FastAPI(title="My FastAPI App")

    # user router をまとめて include
    app.include_router(user_router)

    return app
