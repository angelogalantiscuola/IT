
## API

`An API or Application Programming Interface, is a set of rules and specifications that define how two pieces of software can communicate with each other`. It provides a way for two applications to share data and functionality without having to know the internal workings of the other application.

## Web API

`A web API is an application programming interface (API) that is designed to be accessed over the World Wide Web (WWW)`. It is a set of rules and specifications that define how two systems can communicate with each other. Web APIs are typically accessed using HTTP requests, which are sent from a client application to a server. The server then processes the request and returns a response, which can be in the form of JSON, XML, or another data format.


## More on API

An API is an Application Programming Interface. **It is a way for different programs or applications to communicate with each other** and exchange information or services.
For example, when you use an app like Facebook or Spotify, you are using their API to access their data and features. You don't need to know how they store their data or how they process your requests, you just need to follow their rules and instructions on how to use their API.

> A simple analogy for an API is a waiter in a restaurant. You can see the menu, which tells you what dishes are available and how to order them, but you can't go into the kitchen and cook them yourself. You have to use the waiter, who is the API, to take your order and bring you the food. The waiter knows how to communicate with the kitchen and deliver the food to you, but you don't need to know the details of how they do it.

APIs are a type of **[interface](interface.md)** that enable different applications to communicate and exchange data or functionality. APIs are not the only type of interface in programming, but they are one of the most common and widely used ones.

**An API is a set of rules and protocols that define how different software components or applications can communicate and exchange data or functionality.**
An API specifies what inputs and outputs are expected, what formats are used, and what errors may occur.
An API also provides documentation and examples for developers to follow and understand how to use it.

For example, suppose you have an API that allows you to access weather data from a web service.
The interface of the API would tell you what parameters you need to provide to request the data, such as location, date, and time.
The interface of the API would also tell you what format the data will be returned in, such as JSON or XML.
The interface of the API would also tell you what possible errors you may encounter, such as invalid parameters, network issues, or server errors.

An API can be seen as a **contract between a provider and a consumer of a service or data**. The provider exposes some functionality or data through the API, and the consumer uses the API to access it. The provider does not need to reveal the internal details or implementation of the service or data, and the consumer does not need to know how the provider works. They only need to agree on the API specification and follow it.


## Library vs API

> An analogy for an API and a library is a restaurant menu and a kitchen. The menu is the API that tells you what dishes are available and how to order them. The kitchen is the library that contains the ingredients and equipment to prepare the dishes. You don't need to know how the kitchen works or what recipes it uses, you only need to follow the menu's instructions to get your food.

**A library is a collection of reusable code** that provides some functionality or service.
**An API is an interface that defines how to use and interact with a library** or another software component. An API specifies what methods, parameters, data types, and return values are available and expected. A library can have one or more APIs, depending on how it exposes its functionality to different users or scenarios.

For example, suppose you want to use a library that performs some mathematical operations, such as calculating the square root of a number. The library contains the code that implements the algorithm for finding the square root, but you don't need to know or care about how it does it. You only need to know how to call the library's method that takes a number as an input and returns its square root as an output. That method is part of the API of the library, which tells you what name, arguments, and return type it has.
