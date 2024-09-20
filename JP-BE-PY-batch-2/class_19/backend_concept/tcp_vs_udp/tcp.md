# TCP (Transmission Control Protocol)

TCP (Transmission Control Protocol) is one of the core protocols of the Internet Protocol (IP) suite, commonly referred to as TCP/IP. It ensures reliable, ordered, and error-checked delivery of data between applications running on hosts in a network.

## How TCP Works

- **Connection-Oriented**: Before any data is sent, TCP establishes a connection between the sender and receiver using a process known as a three-way handshake (SYN, SYN-ACK, ACK).
  
- **Reliable Data Transfer**: TCP guarantees that data is delivered correctly and in the proper order. If packets are lost, TCP will retransmit them.
  
- **Flow Control**: TCP uses flow control to ensure that the sender doesn’t overwhelm the receiver with too much data at once.
  
- **Error Checking**: TCP checks for errors in the data through checksums. If errors are detected, it requests a retransmission.
  
- **Congestion Control**: TCP manages network congestion by adjusting the rate at which data is sent, based on the current network conditions.

- **Faster Data Packets Delivery**: Some routes may be faster than others. By allowing packets to take different paths, the network can potentially optimize delivery times based on current conditions.

## Common Applications of TCP

Common applications that use TCP include:

- Web browsing (HTTP/HTTPS)
- Email (SMTP)
- File transfer (FTP)




# TCP vs UDP

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the most widely used transport layer protocols in networking. While both serve the purpose of sending data between devices over the internet, they differ in how they achieve this.

## Key Differences Between TCP and UDP

| Feature                | TCP (Transmission Control Protocol)              | UDP (User Datagram Protocol)                |
|------------------------|--------------------------------------------------|---------------------------------------------|
| **Connection**          | Connection-oriented (requires a handshake)       | Connectionless (no handshake, no connection)|
| **Reliability**         | Ensures reliable delivery of data (error checking, retransmission of lost packets) | No guarantee of data delivery or order      |
| **Ordering**            | Data is guaranteed to arrive in order            | No ordering of packets, they may arrive out of order |
| **Speed**               | Slower due to error checking and flow control    | Faster due to lack of overhead from connection setup or error handling |
| **Use Cases**           | Best for applications requiring reliability (e.g., web browsing, email, file transfer) | Best for applications needing speed and tolerating some data loss (e.g., live streaming, online gaming, VoIP) |
| **Error Checking**      | Extensive error checking and correction          | Basic error checking via checksums, no retransmission |
| **Header Size**         | Larger (20-60 bytes) due to additional features  | Smaller (8 bytes), leading to reduced overhead |
| **Flow Control**        | Uses flow control to avoid overwhelming the receiver | No flow control, sender can transmit as fast as the network allows |
| **Congestion Control**  | Manages congestion by adjusting data transmission rate based on network conditions | No congestion control mechanisms |

## Use Cases

- **TCP**: Web browsing (HTTP/HTTPS), email (SMTP), file transfers (FTP)
- **UDP**: Online gaming, video streaming, VoIP (Voice over IP)

## Summary

- **TCP** is reliable, connection-based, and ensures data integrity at the cost of speed, making it ideal for applications that require accurate delivery of data.
- **UDP** is faster and connectionless but lacks reliability, making it suitable for applications where speed is more important than perfect data accuracy.
