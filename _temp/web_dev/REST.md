
- [REST](#rest)
  - [1. representation of a resource](#1-representation-of-a-resource)
  - [2. transferring representation](#2-transferring-representation)
  - [3. principles](#3-principles)
    - [3.1. HTTP](#31-http)
    - [3.2. URLs](#32-urls)
  - [4. RESTful API](#4-restful-api)



**REST** stands for **RE**presentational **S**tate **T**ransfer. **It’s a way for two different programs to talk to each other over the internet.** For example, you might use a program on your phone to check the weather. That program needs to get the weather information from another program that runs on a big computer somewhere else. To do that, they use REST.

**REST is a software architectural style** that describe a way of designing web services that follows some principles and constraints, such as:

- using HTTP methods,
- identifying resources with URLs (see ==endpoint==),
- transferring representations of resources between clients and servers.

The name implies that **each program can represent the state of a resource in different ways, depending on the needs and preferences of the program**. For example, a resource can be represented as text, XML, JSON, HTML, or any other format that can be transferred over HTTP.


## In depth


REST, which stands for Representational State Transfer, is an `architectural style for designing and developing APIs` (==Application Programming Interfaces==) It is a set of principles that define how two pieces of software can communicate with each other. RESTful APIs are designed to be lightweight, scalable, and easy to use.

**Key principles of REST:**

1. `Client-server architecture`: RESTful APIs follow a client-server architecture, where clients send requests to a server, and the server processes those requests and returns responses.

2. `Statelessness`: RESTful APIs are stateless, meaning that each request from a client contains all the information necessary to fulfill the request. The server does not store any information about the client's previous requests.

3. `Cacheable data`: RESTful APIs should be designed to allow clients and intermediaries to cache responses to improve performance.

4. `Uniform interface`: RESTful APIs should have a uniform interface, meaning that all resources are accessed using the same set of methods and operations.



## 1. representation of a resource

The representation of a resource is **the way that the resource is formatted or encoded for communication**.
A resource can be anything that can be **identified by a URL**, such as a user, a file, or a weather report. A representation is how the resource is expressed in a specific format, such as JSON, XML, or HTML.
For example, a resource that represents a user might have different representations in JSON and XML.

``` json
{ "id": 1, "name": "Alice", "email": "alice@example.com" }
```

``` xml
<user> <id>1</id> <name>Alice</name> <email>alice@example.com</email> </user>
```

## 2. transferring representation

The concept of transferring representations of resources between clients and servers means that the client can request or send a specific representation of a resource using HTTP methods and headers.

For example, a client can use the GET method to ask for the user resource in JSON format by specifying the Accept header: `GET /users/1 Accept: application/json`
The server can respond with the JSON representation of the user resource and specify the Content-Type header:  `HTTP/1.1 200 OK Content-Type: application/json`

``` json
{ "id": 1, "name": "Alice", "email": "alice@example.com" }
```

Similarly, a client can use the PUT method to update the user resource by sending a new representation in XML format and specifying the Content-Type header: `PUT /users/1 Content-Type: application/xml`

``` xml
<user> <id>1</id> <name>Alice</name> <email>alice@newdomain.com</email> </user>
```

The server can respond with an appropriate status code and optionally send back a representation of the updated resource: `HTTP/1.1 200 OK Content-Type: application/xml`

This way, the client and server can exchange different representations of the same resource depending on their needs and preferences. The representation of a resource can also include links to other related resources, which is called hypermedia. For example, a JSON representation of a user resource might include links to their posts and comments:

``` json
{
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "links": [
        {
            "rel": "posts",
            "href": "/users/1/posts"
        },
        {
            "rel": "comments",
            "href": "/users/1/comments"
        }
    ]
}
```

## 3. principles

Some of the main principles and constraints of REST are:

- **Client-server**: The client and the server are separate entities that communicate through a standardized interface.

- **Stateless**: The server does not store any information about the client’s state or session. Each request from the client contains all the necessary information for the server to process it.

- **Cacheable**: The server can indicate whether its responses are cacheable or not, so that the client and intermediate components can store them and reuse them to improve performance and reduce network traffic.

- **Layered system**: The client does not need to know whether it is communicating directly with the server or with an intermediary component, such as a proxy or a load balancer. This allows for scalability, security, and modularity of the system.

- **Uniform interface**: The client and the server use a common language to exchange resources, such as HTTP methods (GET, POST, PUT, DELETE) and media types (JSON, XML, HTML). Each resource is identified by a unique URL (Uniform Resource Locator) and can have different representations depending on the client’s preferences.

- **Code on demand** (optional): The server can send executable code to the client, such as JavaScript or Java applets, to extend its functionality.

### 3.1. HTTP

One of the rules is that they **use the same language that your web browser uses to get web pages.** That language is called HTTP. HTTP has some words that tell what kind of thing you want to do with a web page. For example:

- **GET** means you want to see a web page,
- **POST** means you want to send some information to a web page,
- **PUT** means you want to change something on a web page,
- **DELETE** means you want to remove something from a web page.

### 3.2. URLs

**Another rule is that they use special names for the things they want to talk about.** These names are called URLs, and they look like this: <https://example.com/weather/city/paris>. This URL tells you that the thing we want to talk about is the weather in Paris. The programs can use these URLs to ask for or change information about those things.

For example, if your phone program wants to know the temperature in Paris, it can send a **GET** request with this URL: <https://example.com/weather/city/paris/temperature>. The big computer program will look up the temperature and send it back as a response. The response might look like this: ``{"temperature": 15}``. This means that the temperature is 15 degrees Celsius.

If your phone program wants to change the temperature in Paris (maybe you’re feeling mischievous), it can send a **PUT** request with this URL: <https://example.com/weather/city/paris/temperature>. It also needs to send some information about what it wants to change it to. For example, it might send this: ``{"temperature": 30}``. The big computer program will check if it’s allowed to do that, and if so, it will change the temperature and send back a response. The response might look like this: ``{"status": "OK"}``. This means that everything went well.

If your phone program wants to delete the temperature in Paris (maybe you’re feeling evil), it can send a **DELETE** request with this URL: <https://example.com/weather/city/paris/temperature>. The big computer program will check if it’s allowed to do that, and if so, it will delete the temperature and send back a response. The response might look like this: ``{"status": "OK"}``.

## RESTful API

REST stands for REpresentational State Transfer, which is a software architecture that defines how different programs can communicate with each other over the internet using HTTP (Hypertext Transfer Protocol)

RESTful API is **a type of API that follows the principles and constraints of REST**.

**So, REST is an architectural style, while RESTful API is an implementation of that style.**

The main difference between API and REST API is that API is a broad term that covers any kind of interface between software applications, while REST API is a specific kind of web API that follows a certain architectural style. **Not all APIs are RESTful, but all RESTful APIs use REST.**

## RESTful API interaction

1. **Client sends a request:** A client application, such as a web browser or mobile app, sends an HTTP request to the server hosting the RESTful API. The request includes the following information:

    * **HTTP method:** The HTTP method specifies the type of operation the client wants to perform, such as GET (retrieve data), POST (create data), PUT (update data), or DELETE (remove data).

    * **URI (Uniform Resource Identifier):** The URI identifies the specific resource the client wants to access, such as /users/123 to retrieve data about a specific user.

    * **Headers:** Headers provide additional information about the request, such as authentication credentials or content type.

    * **Body:** The body of the request can optionally contain data to be sent to the server, such as a new user record to be created.

2. **Server processes the request:** The server receives the HTTP request and processes it according to the RESTful principles. It validates the request, identifies the resource, and performs the requested operation.

3. **Server sends a response:** The server sends an HTTP response back to the client. The response includes the following information:

    * **HTTP status code:** The HTTP status code indicates whether the request was successful or not. Common status codes include 200 (OK), 400 (Bad Request), 404 (Not Found), and 500 (Internal Server Error).

    * **Headers:** Headers provide additional information about the response, such as the content type of the response data.

    * **Body:** The body of the response contains the requested data or an error message if the request failed.

4. **Client receives the response:** The client receives the HTTP response and processes it. It extracts the data from the response body and displays it to the user or updates the application's state accordingly.

This process repeats for each interaction between the client and the server. RESTful APIs allow for a seamless exchange of data and functionality between different applications and services.
