from fastapi import FastAPI
from app.route.app_route import router as app_router

def create_app() -> FastAPI:
    app = FastAPI(title="My FastAPI App")

    # 全体 router をまとめて include
    app.include_router(app_router)

    return app
