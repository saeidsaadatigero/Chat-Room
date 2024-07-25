from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    user_id: str
    email: str
    name: str
    online_status: bool

class Message(BaseModel):
    sender_id: str
    receiver_id: str
    room_id: str
    content: str
    timestamp: str


class Message(BaseModel):
    id: str
    username: str
    content: str
