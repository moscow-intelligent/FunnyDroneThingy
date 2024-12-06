import websocket
import json
import threading

class GameClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.ws = None
        self.thread = None
        self.other_clients_coordinates = {}  # Store coordinates of other clients

    def on_message(self, ws, message):
        """Callback function to handle incoming messages."""
        data = json.loads(message)
        if data["type"] == "map":
            print("Received map data:", data["data"])
        elif data["type"] == "coordinates":
            # Handle received coordinates from another client
            data = data['data']
            client_id = data.get("client_id", "unknown")  # Assuming client_id is sent
            coordinates = data["coordinates"]
            self.other_clients_coordinates[client_id] = coordinates
            print(f"Received coordinates from client {client_id}: {coordinates}")
            self.update_game_state(client_id, coordinates)

    def on_error(self, ws, error):
        """Callback function to handle errors."""
        print("Error:", error)

    def on_close(self, ws):
        """Callback function to handle connection closure."""
        print("Connection closed")

    def on_open(self, ws):
        """Callback function to handle successful connection."""
        print("Connected to the server")

    def run(self):
        """Run the WebSocket client."""
        #websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.server_url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.cords = {}
        self.thread.start()

    def send_coordinates(self, coordinates, name):
        """Send coordinates to the server."""
        if self.ws:
            # Include a client_id in the message
            message = {
                "client_id": name,  # Replace with actual client ID
                "coordinates": coordinates
            }
            self.ws.send(json.dumps(message))
            print("Sent coordinates:", coordinates)

    def update_game_state(self, client_id, coordinates):
        """Update the game state based on received coordinates."""
        # Implement your game logic here
        # For example, you could update the position of other players on the screen
        self.cords[client_id] = coordinates
        print(f"Updating game state for client {client_id} at {coordinates}")

    def close(self):
        """Close the WebSocket connection."""
        if self.ws:
            self.ws.close()
            self.thread.join()

# Example usage
if __name__ == "__main__":
    client = GameClient("ws://localhost:8765")
    client.run()

    # Simulate sending coordinates on certain events
    try:
        while True:
            # Replace this with your event detection logic
            event = input("Enter coordinates to send (x,y) or 'exit' to quit: ")
            if event.lower() == 'exit':
                break
            try:
                x, y = map(int, event.split(','))
                client.send_coordinates({"x": x, "y": y})
            except ValueError:
                print("Invalid input. Please enter coordinates in the format x,y.")
    finally:
        client.close()
