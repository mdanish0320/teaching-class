# Comparison of HTTP Versions

## HTTP/1.0
- **Release Year**: 1996
- **Key Features**:
  - Basic request/response model.
  - Each request opens a new TCP connection.
  - No persistent connections or caching mechanisms.
  
- **Limitations**:
  - **Connection Overhead**: Each request requires a new TCP connection, leading to increased latency and resource consumption.
  - **No Caching**: Lack of caching capabilities resulted in repeated data transfer, making it inefficient for frequently accessed resources.

## HTTP/1.1
- **Release Year**: 1999
- **Key Features**:
  - Persistent connections by default (keep-alive).
  - Chunked transfer encoding.
  - Additional cache control headers.
  - Support for pipelining (sending multiple requests without waiting for responses).

- **Limitations**:
  - **Head-of-Line Blocking**: In pipelining, if one request is delayed, all subsequent requests are blocked, causing latency.
  - **Limited Multiplexing**: While persistent connections reduced connection overhead, they still couldn’t handle multiple simultaneous requests efficiently.
  
## HTTP/2
- **Release Year**: 2015
- **Key Features**:
  - Binary framing layer, allowing for multiplexing multiple streams over a single connection.
  - Header compression (HPACK) to reduce overhead.
  - Server push capabilities, allowing servers to send resources to clients proactively.

- **Limitations**:
  - **Complexity**: The binary format and framing mechanisms introduce complexity in implementation and debugging.
  - **TLS Requirement**: Although not mandatory, HTTP/2 is often used over TLS, which adds overhead and may complicate setups.

## HTTP/3
- **Release Year**: 2020
- **Key Features**:
  - Based on QUIC (Quick UDP Internet Connections), using UDP instead of TCP.
  - Improved connection establishment time due to 0-RTT handshakes.
  - Better handling of packet loss and reduced latency.

- **Limitations**:
  - **Adoption**: As a newer protocol, widespread adoption and support from web servers, browsers, and CDNs are still growing.
  - **Firewall Issues**: QUIC’s use of UDP may face challenges with firewalls and NATs, as UDP traffic can be less predictable.

## Summary of Limitations Leading to Development
- **HTTP/1.0**: High connection overhead and lack of caching.
- **HTTP/1.1**: Head-of-line blocking and limited multiplexing capabilities.
- **HTTP/2**: Complexity in implementation and TLS overhead.
- **HTTP/3**: Adoption challenges and potential firewall issues.

Each version of HTTP aimed to address the limitations of its predecessor while introducing new features to enhance web performance and user experience.
