from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from database import connect_to_mongo
import jwt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


app.include_router(router)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Chat Room API!"}


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{username} says: {data}")


