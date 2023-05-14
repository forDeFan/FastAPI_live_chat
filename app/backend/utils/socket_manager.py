from typing import List

from fastapi import WebSocket


class SocketManager:
    """
    Class to manage websocket connections.
    """

    def __init__(self) -> None:
        self.active_connections: List[(WebSocket, str)] = []

    async def connect(self, websocket: WebSocket, user: str) -> None:
        """Connect client to websocket."""
        await websocket.accept()
        self.active_connections.append((websocket, user))

    def disconnect(self, websocket: WebSocket, user: str) -> None:
        """Disconnect client from websocket."""
        self.active_connections.remove((websocket, user))

    async def broadcast(self, data: dict[str]) -> dict[str]:
        """Bidirectional communication in active connection state."""
        for connection in self.active_connections:
            await connection[0].send_json(data)
