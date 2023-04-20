# Interface

> An analogy for an interface is a light switch. A light switch is an interface that allows you to turn on or off a light. You don't need to know how the switch works internally, or how it connects to the electrical system. You only need to know that it has two states (on or off) and that it responds to your input (flipping it). Different types of switches can implement the same interface in different ways, such as a toggle switch, a push button switch, or a dimmer switch.

An interface in programming is a more general term that can refer to **any point of interaction between two or more components of a system**

- An interface can be between hardware and software, software and software, software and user, or user and user.
- An interface defines the format, protocol, and rules for exchanging information or commands between the components.
- An interface can be graphical, textual, auditory, tactile, or any other mode of communication.

For example, suppose you have a computer system that consists of a keyboard, a mouse, a monitor, a printer, an operating system, and an application.
Each of these components has an interface with one or more other components.
The keyboard and the mouse have a hardware interface with the computer that specifies how they send signals to the operating system.
The monitor and the printer have a hardware interface with the computer that specifies how they receive signals from the operating system.
The operating system and the application have a software interface that specifies how they communicate with each other.
The application and the user have a user interface that specifies how they interact with each other through graphical elements or commands.

## Examples of interfaces in programming

- A **graphical user interface (GUI)** that allows the user to interact with an application through visual elements such as buttons, menus, icons, etc.
- A **command-line interface (CLI)** that allows the user to interact with an application through text commands and responses.
- A **web service interface** that allows different applications to communicate with each other over the internet through standard protocols such as HTTP and XML.
- A **database interface** that allows an application to access and manipulate data stored in a database system through queries and statements.
- A **hardware interface** that allows a device to communicate with a computer system through signals and wires.

## Interface in OOP

An interface is **a way of describing the actions or behaviors that an object can do, without specifying how they are implemented.** An interface defines a set of methods, properties, events, or other members that an object must have in order to be considered as an instance of that interface. An interface is like a *contract* that an object agrees to follow when it implements the interface.

For example, suppose you have an interface called IAnimal that defines a method called MakeSound. Any class that implements this interface must provide a definition for this method, otherwise it will not compile. The interface does not care how the method is implemented, as long as it exists and has the same signature (name, parameters, and return type). Different classes can implement the same interface in different ways, depending on their logic and purpose.
