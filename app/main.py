import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.infra.web.router import setup_routers
from app.playground.calculator import build_calculator_demo

app = FastAPI()
setup_routers(app)
lambda_handler = Mangum(app)


@app.get("/")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, Subnet Calculator!"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )
