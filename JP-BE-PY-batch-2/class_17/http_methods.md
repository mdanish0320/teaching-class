# HTTP Methods Overview

HTTP methods are used to indicate the desired action to be performed on a resource in a web request. Each method serves a specific purpose:

- **GET**: Retrieves data from a server. This method is used to request data from a specified resource and should not alter any data on the server.
- **POST**: Submits data to be processed by the server. It is commonly used for creating new resources.
- **PUT**: Updates an existing resource or creates a new resource if it doesn't exist. The client must send the entire resource with this request.
- **DELETE**: Removes a specified resource from the server.
- **PATCH**: Partially updates an existing resource. This method allows for modifying only certain fields without sending the entire resource.
- **OPTIONS**: Describes the communication options for the target resource, often used in CORS preflight requests. For example, an `OPTIONS` request to `/api/user/123` might indicate allowed methods like `GET`, `PUT`, and `DELETE`.

## Other HTTP Methods

- **HEAD**: Similar to `GET`, but it retrieves only the headers, not the body of the response.
- **TRACE**: Echoes the received request, primarily for debugging purposes.
- **CONNECT**: Establishes a tunnel to the server, commonly used for HTTPS requests.

Each HTTP method serves a distinct role in web communication, enabling various operations on resources.
