from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client.chat_service

async def connect_to_mongo():
    db.users.create_index("email", unique=True)

from fastapi import FastAPI, WebSocket
from bson import ObjectId

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client.chat_db  # Your database name
messages_collection = db.messages  # Your collection name
