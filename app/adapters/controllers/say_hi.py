from fastapi import APIRouter, status

say_hi_routes = APIRouter(tags=["say_hi"], prefix="/say_hi")

@say_hi_routes.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "Hi, I'm alive!"}

@say_hi_routes.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": "pong"}

@say_hi_routes.get("/echo", status_code=status.HTTP_200_OK)
async def echo(message: str):
    return {"message": message}
