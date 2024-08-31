
# Localhost

Both localhost and 127.0.0.1 refer to the same thing: the local loopback address of your computer. However, there are subtle differences between them:

- **127.0.0.1**: The numeric IPv4 loopback address; no DNS resolution needed.
- **localhost**: A hostname that resolves to the loopback address (127.0.0.1 for IPv4 or ::1 for IPv6) via DNS or the hosts file.

# IP Address and Port

An IP address (Internet Protocol address) is a unique identifier assigned to each device connected to a network that uses the Internet Protocol for communication.

- **Local IP address command**: `ipconfig`
- **Public IP and Private IP**
- **IP Address** is the address of the machine on the network.
- **Port** is the address of the application in the machine.

## Port Number

A port number is an integer between 0 and 65535. It helps the operating system's networking stack determine which application or service should handle incoming network traffic.

## Network Traffic

When data is sent over the internet or a local network, it needs to be delivered to the correct application on the receiving machine. The IP address identifies the machine, and the port number identifies the specific application or service.

## Common Ports

- **80**: The default port for HTTP traffic.
- **443**: The default port for HTTPS traffic (secure HTTP).
- **5000**: The default port for a Flask development server.
