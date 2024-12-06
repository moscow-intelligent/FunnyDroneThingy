import asyncio
import websockets
import json

# Set to hold connected clients
connected_clients = set()

# Sample map data
map_data = {
    "width": 10,
    "height": 10,
    "terrain": "grass"
}

async def broadcast(message):
    """Send a message to all connected clients."""
    if connected_clients:  # Check if there are any connected clients
        for client in connected_clients:
            await client.send(message)
async def handler(websocket, path):
    """Handle incoming WebSocket connections."""
    # Register the new client
    connected_clients.add(websocket)
    try:
        # Send map data to the newly connected client
        await websocket.send(json.dumps({"type": "map", "data": map_data}))

        async for message in websocket:
            # Process incoming messages (coordinates)
            data = json.loads(message)
            if "coordinates" in data:
                # Broadcast the coordinates to all clients
                await broadcast(json.dumps({"type": "coordinates", "data": data}))
    finally:
        # Unregister the client when done
        connected_clients.remove(websocket)

async def main():
    """Start the WebSocket server."""
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
