from fastapi import FastAPI
from app.crud.create.route import router as create_router
from app.crud.get.route import router as get_router
from app.crud.put.route import router as update_router
from app.crud.delete.route import router as delete_router

def create_app() -> FastAPI:
    app = FastAPI(title="My FastAPI App")

    app.include_router(create_router)
    app.include_router(get_router)
    app.include_router(update_router)
    app.include_router(delete_router)

    return app
