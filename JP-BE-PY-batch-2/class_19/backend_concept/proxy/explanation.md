| Feature               | Forward Proxy                          | Reverse Proxy                           |
|-----------------------|---------------------------------------|-----------------------------------------|
| **Definition**        | Intermediary for clients to access resources from servers. | Intermediary for servers to handle client requests. |
| **Client Awareness**   | Clients must configure proxy settings. | Clients are unaware; they see only the proxy. |
| **Use Cases**         | - Anonymity <br> - Content filtering <br> - Caching <br> - Access control | - Load balancing <br> - SSL termination <br> - Caching <br> - Security |
| **Direction of Traffic** | Client → Forward Proxy → Server   | Client → Reverse Proxy → Server         |
| **Visibility**        | Client IP is hidden from the server. | Backend server details are hidden from clients. |
| **Main Role**        | Enhances client-side functions.      | Enhances server-side functions.         |
