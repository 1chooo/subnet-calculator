import gradio as gr
from fastapi import FastAPI

from app.adapters.controllers.mock import mock_routes
from app.adapters.controllers.say_hi import say_hi_routes
from app.playground.calculator import build_calculator_demo


def setup_routers(app: FastAPI) -> None:
    """
    Setup routers for the application

    Args:
        - app (FastAPI): FastAPI instance

    Returns:
        - None
    """
    gr.mount_gradio_app(app, build_calculator_demo(), path="/playground/subnet_calculator")
    app.include_router(say_hi_routes)
    app.include_router(mock_routes)
