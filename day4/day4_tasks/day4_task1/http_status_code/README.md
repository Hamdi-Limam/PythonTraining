## HTTP Status Codes

REST APIs use the Status-Line part of an HTTP response message **to inform clients of their request’s overarching result**. [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) defines the [Status-Line syntax](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html#sec6.1) as shown below:
> Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF

HTTP defines these standard status codes that can be used to convey the results of a client’s request. The status codes are divided into the five categories.
- 1xx: Informational – Communicates transfer protocol-level information.
- 2xx: Success – Indicates that the client’s request was accepted successfully.
- 3xx: Redirection – Indicates that the client must take some additional action in order to complete their request.
- 4xx: Client Error – This category of error status codes points the finger at clients.
- 5xx: Server Error – The server takes responsibility for these error status codes.

Here is a list of HTTP status codes with their descriptions. [Click here](https://restfulapi.net/http-status-codes/).

## Examples of REST Specific Status Codes

### 200 (OK)
It indicates that the REST API **successfully carried out whatever action the client requested** and that no more specific code in the 2xx series is appropriate.

Unlike the 204 status code, a 200 response **should include a response body**. The information returned with the response is dependent on the method used in the request.

### 201 (Created)
A REST API responds with the 201 status code whenever **a resource is created inside a collection**. There may also be times when a new resource is **created as a result of some controller action**, in which case 201 would also be an appropriate response.

The origin server MUST create the resource **before returning the 201 status code**. If the action cannot be carried out immediately, the server SHOULD respond with a `202 (Accepted)` response instead.

### 202 (Accepted)
A 202 response is typically **used for actions that take a long while to process**. It indicates that the request has been accepted for processing, but the processing **has not been completed**. The request might or might not be eventually acted upon, or even maybe disallowed when processing occurs.

Its purpose is to allow a server to accept a request for some other process without requiring that the user agent’s connection to the server persist until the process is completed.

The entity returned with this response SHOULD include an indication of the request’s current status and either a pointer to a status monitor (job queue location) or some estimate of when the user can expect the request to be fulfilled.

### 204 (No Content)
The 204 status code is usually sent out in response to a PUT, POST, or DELETE request when the REST API **declines to send back any status message or representation in the response message’s body**.

An API may also send 204 in conjunction with a GET request to indicate that the requested resource exists, but has **no state representation** to include in the body.

### 400 (Bad Request)
400 is the generic client-side error status, used when no other 4xx error code is appropriate. Errors can be like **malformed request syntax, invalid request message parameters, or deceptive request routing** etc.

The client SHOULD NOT repeat the request without modifications.

### 401 (Unauthorized)
A 401 error response indicates that the client tried to operate on a protected resource **without providing the proper authorization**. It may have provided the **wrong credentials or none at all**. The response must include a WWW-Authenticate header field containing a challenge applicable to the requested resource.

### 403 (Forbidden)
A 403 error response indicates that the client’s request is formed correctly, but the **REST API refuses to honor it**, i.e., the user does not have **the necessary permissions** for the resource. A 403 response is not a case of insufficient client credentials; that would be 401 `(“Unauthorized”)`.

### 404 (Not Found)
The 404 error status code indicates that the **REST API can’t map the client’s URI to a resource** but may be available in the future. Subsequent requests by the client are permissible.

### 500 (Internal Server Error)
500 is the generic REST API error response. Most web frameworks automatically respond with this response status code whenever **they execute some request handler code that raises an exception**.

###  501 (Not Implemented)
The server either does **not recognize the request method, or it cannot fulfill the request**. Usually, this implies future availability (e.g., a new feature of a web-service API).