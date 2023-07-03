from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict: #Assync sirve para que si no la llame no gaste memoria
    return {
    "message": "Hello World"
    }

app.include_router(todo_router)
