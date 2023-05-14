from fastapi import (APIRouter, WebSocket, WebSocketDisconnect)
from ..utils.socket_manager import SocketManager

socket_router = APIRouter()
manager: SocketManager = SocketManager()


@socket_router.websocket("/api/chat")
async def socket(websocket: WebSocket):
    """\f Main websocket function to coordinate bidirectional communication."""
    sender: str = websocket.cookies.get("X-Authorization")
    if sender:
        await manager.connect(websocket, sender)
        response: dict[str, str] = {
            "sender": sender,
            "message": "Join chatroom",
        }
        await manager.broadcast(response)
        try:
            while True:
                data: dict[str, str] = await websocket.receive_json()
                await manager.broadcast(data)
        except WebSocketDisconnect:
            manager.disconnect(websocket, sender)
            response["message"]: str = "Left chatroom"
            await manager.broadcast(response)