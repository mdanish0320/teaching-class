# Communication Patterns between Client and Server

## 1. Request/Response (Client → Server)
Request/Response is the most common communication pattern used on the web. In this model:
- The **client** sends a **request** to the **server**.
- The server processes the request and returns a **response**.
- The communication is synchronous, meaning the client waits for the server's response before continuing.
  
  **Example**: A browser requests a webpage, and the server responds with the HTML content.

## 2. Polling (Client → Server)
Polling is a technique used when the client needs to receive updates from the server regularly:
- The client repeatedly sends requests to the server at regular intervals (e.g., every few seconds).
- The server responds with any new data.
- Polling can be inefficient because the server is queried regardless of whether there is new data.

  **Example**: A client checking for new messages in a chat application every 5 seconds.

## 3. Long Polling (Client → Server)
Long Polling is an improvement over standard polling:
- The client sends a request to the server.
- The server holds the request open until new data is available.
- Once the server has new data, it responds to the client.
- After receiving the response, the client immediately sends a new request, and the cycle repeats.

  **Example**: A real-time notification system where the client wants to be informed as soon as new events occur.

## 4. Server-Sent Events (Uni-directional)
Server-Sent Events (SSE) allow the server to send updates to the client over an open connection:
- The client establishes a connection to the server.
- The server continuously sends events to the client as they become available.
- Communication is **uni-directional** (server to client only).

  **Example**: Live sports scores or stock price updates delivered from the server to the client without the client requesting them each time.

## 5. Push (Bi-directional)
Push communication is **bi-directional**, meaning both the client and the server can send messages to each other:
- A connection (often WebSocket) is established between the client and server.
- Both client and server can push messages through the same connection without needing to re-establish the connection for each message.

  **Example**: A live chat application where both parties can send and receive messages in real-time.

## 6. Pub/Sub (Client → Broker → Server) (Topics/Subscribers)
The Publish/Subscribe (Pub/Sub) model decouples the client from the server by introducing a **broker**:
- The **client** (subscriber) subscribes to a specific topic with a broker.
- The **server** (publisher) sends messages to the broker, which distributes them to all subscribers.
- Subscribers receive updates without directly communicating with the server.

  **Example**: A news system where users subscribe to specific topics and receive updates whenever new articles are published in those topics.
