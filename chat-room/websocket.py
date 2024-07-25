from fastapi import WebSocket, APIRouter, WebSocketDisconnect
from fastapi.responses import HTMLResponse

router = APIRouter()

active_connections: dict = {}

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    active_connections[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast the message to all connected clients
            for connection in active_connections.values():
                await connection.send_text(f"{user_id}: {data}")
    except WebSocketDisconnect:
        # Remove the connection if the client disconnects
        del active_connections[user_id]
        for connection in active_connections.values():
            await connection.send_text(f"{user_id} has left the chat.")
    except Exception as e:
        print(f"Error: {e}")
        del active_connections[user_id]
