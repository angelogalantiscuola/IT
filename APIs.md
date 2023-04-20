# APIs

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

## types of APIs

There are many ways to classify APIs based on different criteria, such as **protocol, architecture, format, or scope**.
One common way to categorize APIs is by their intended scope of use, which indicates who can access and use them. According to this criterion, there are four main types of APIs:

- **Public APIs**: These are APIs that are open and available for anyone to use. They are also called open or external APIs. They usually have minimal or no authentication or authorization requirements, and they may be monetized by charging a fee per API call. Examples of public APIs are Google Maps API, Twitter API, or Spotify API.
- **Partner APIs**: These are APIs that are restricted and available only for specific and authorized partners or businesses. They are also called B2B APIs. They usually have stronger authentication and authorization mechanisms, and they may not be monetized directly, but rather through a partnership agreement. Examples of partner APIs are PayPal API, Stripe API, or Amazon MWS API.
- **Internal APIs**: These are APIs that are private and available only for internal use within an organization. They are also called private APIs. They usually have weak or no authentication or authorization requirements, as they rely on other security policies within the organization. They are not monetized at all, but rather used to improve efficiency and productivity. Examples of internal APIs are Salesforce API, SAP API, or Oracle API.
- **Composite APIs**: These are APIs that combine data or functionality from multiple other APIs into a single API call. They are also called mashup APIs. They can be any of the above types of APIs depending on their scope and access level. They are used to simplify complex workflows and reduce latency and bandwidth consumption. Examples of composite APIs are Twilio API, Zapier API, or IFTTT API.

These are not the only types of APIs, but they are some of the most common ones. Other types of APIs may be based on different criteria, such as protocol (e.g., SOAP, REST, GraphQL), architecture (e.g., microservices, serverless), format (e.g., JSON, XML), or domain (e.g., social media, e-commerce).

A [**RESTful API**](REST.md) is an API that follows these constraints and provides a simple, uniform, and scalable way to access web resources. A RESTful API is not the only type of API, but it is one of the most popular and widely used ones.

## Difference between an API, a library, and a function

### Function vs library

> An analogy for a library and a function is a book and a chapter. A book is a collection of chapters that provide some information or knowledge. A book can contain one or more chapters, depending on how it organizes its content. A chapter is a section of text that covers a specific topic and can be read independently. A chapter has a title, a number, and a summary. A chapter can be written by the author or by another source.

**A function is a block of code** that performs a specific task and can be reused in different places. A function has a name, a set of parameters, and a return value. A function can be defined by the user or by the library.
**A library is a collection of functions** (and possibly other resources) that provide some functionality or service. A library can contain one or more functions, depending on how it organizes its code.

For example, suppose you want to use a function that calculates the factorial of a number. The factorial of a number n is the product of all positive integers less than or equal to n. The function can be defined by the user as follows:

```python
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)
```

This is a **user-defined function** that can be used in different places in the program.

Alternatively, the function can be provided by a library, such as the math library in Python. The math library contains many functions that perform mathematical operations, such as sqrt, sin, cos, etc. To use the function from the library, you need to import the library and call the function with its name and argument:

```python
import math
math.factorial(5)
```

This is a **library function** that can also be used in different places in the program. The difference is that the user does not need to define or know how the function works internally, as it is already implemented by the library.

### Library vs API

> An analogy for an API and a library is a restaurant menu and a kitchen. The menu is the API that tells you what dishes are available and how to order them. The kitchen is the library that contains the ingredients and equipment to prepare the dishes. You don't need to know how the kitchen works or what recipes it uses, you only need to follow the menu's instructions to get your food.

**A library is a collection of reusable code** that provides some functionality or service.
**An API is an interface that defines how to use and interact with a library** or another software component. An API specifies what methods, parameters, data types, and return values are available and expected. A library can have one or more APIs, depending on how it exposes its functionality to different users or scenarios.

For example, suppose you want to use a library that performs some mathematical operations, such as calculating the square root of a number. The library contains the code that implements the algorithm for finding the square root, but you don't need to know or care about how it does it. You only need to know how to call the library's method that takes a number as an input and returns its square root as an output. That method is part of the API of the library, which tells you what name, arguments, and return type it has.
