from fastapi import FastAPI

from app.backend.routers.chat_router import chat_router
from app.backend.routers.home_router import home_router
from app.backend.routers.socket_router import socket_router
from app.backend.routers.user_router import user_router


def include_router(app: FastAPI) -> None:
    """
    Include API routes into the main app.

    Args:
        app (FastAPI): instance where routers will be added.
    """
    routers = [home_router, chat_router, user_router, socket_router]

    for r in routers:
        app.include_router(router=r)


def start_application() -> FastAPI:
    """
    Start the app and include the routers.

    Returns:
        FastAPI: runnable instance
    """
    app = FastAPI(title="Chat app")
    include_router(app)
    return app


app = start_application()
