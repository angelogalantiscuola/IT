# DB

%% Begin Waypoint %%
- [[ER]]
- [[from_data_to_database]]
- [[normalization]]
- **[ORM](./ORM/ORM.md)**

%% End Waypoint %%

A **database** is a system to store and manage data in a structured and very efficient way.

If you don't know everything about databases, here's a quick overview: [Intro to Databases](https://sqlmodel.tiangolo.com/databases/)

## OOP class model vs DB ER model

Object-Oriented Programming (OOP) UML Class Model and Database Entity-Relationship (ER) Model are both tools used to visually represent and design systems. However, they have different focuses and use different terminologies.

Similarities:

- Both models represent **entities** (classes or tables) and the **relationships** between them.
- Both models can represent **attributes** of entities.
- Both models can represent constraints on entities and relationships.

Differences:

- UML Class Model focuses on the **behavior** of the system, including methods (functions) that can be performed on classes. ER Model does not typically include behavior.
- UML Class Model uses OOP concepts like inheritance, polymorphism, and encapsulation. ER Model does not have these concepts.
- UML Class Model represents relationships using associations, aggregations, and compositions. ER Model uses relationships with cardinality (one-to-one, one-to-many, many-to-many).
- UML Class Model is typically used in the design of **software systems**. ER Model is used in the design of **databases**.
