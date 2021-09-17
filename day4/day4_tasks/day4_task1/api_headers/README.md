## API Headers

### What are API Headers?
API headers are like **an extra source of information** for each API call you make. Their job is **to represent the meta-data associated with an API request and response**.

If you ever encounter issues with an API, the first place you should look is the headers, since they can help you track down any potential issues. This makes them a very important part of each request.

API Headers tell you about:
1. Request and Response Body
2. Request Authorization
3. Response Caching
4. Response Cookies

 ### Where do I see the headers in my API request?

You see headers in the message body. That’s the chunk of data that includes everything in the request or response. The headers usually come after the request line or response line.

Headers all look the same; they have an obvious format that you can spot from a mile away. They are a **key–value pair in clear-text string format** separated by a colon. To see what they look like in practice, check out the example below:
```
{
 "key1": "  value1",
 "key2": " value2",
 "key3": " value3",
}
```
Usually, the strings used are longer and more random. But no matter how long or random a string may look, the general format remains the same: “key” : “value“. To see a list of the most common header fields, [click here](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields).

### Examples of API Headers

Here are some of the most common API Headers you will encounter when testing any API.
* Authorization: Contains the authentication credentials for HTTP authentication.
* WWW-Authenticate: The server may send this as an initial response if it needs some form of authentication before responding with the actual resource being requested. Often following this header is the response code 401, which means “unauthorized”.
* Accept-Charset: This header is set with the request and tells the server which character sets (e.g., UTF-8, ISO-8859-1, Windows-1251, etc.) are acceptable by the client.
* Content-Type:  Tells the client what media type (e.g., application/json, application/javascript, etc.) a response is sent in. This is an important header field that helps the client know how to process the response body correctly.
* Cache-Control: The cache policy defined by the server for this response, a cached response can be stored by the client and re-used till the time defined by the Cache-Control header.

### Final words

API Headers **contain a wealth of information for tracking down potential issues** when using any API.
Most of the time, you won’t be looking at them. But when problems arise, the headers are the first place you should look.