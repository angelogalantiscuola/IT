# Mapping Object Model to Data Model

Generally speaking, the **mapping between class and entity is a one-to-one** mapping, meaning that one class in object model maps with one entity in data model.

![[Pasted image 20240220173042.png]]

Since the classes map to the entities, **attributes map to columns** accordingly.

![[Pasted image 20240220173048.png]]

An attribute of **array** type will be converted to an Array Table.

![[Pasted image 20240220173135.png]]

**Associations and relationships can be mapped from one to the other**, especially when transitioning between UML class diagrams (used in object-oriented design) and ER diagrams (used in database design).

## One-to-One Association

One-to-One Association: This can be directly mapped to a one-to-one relationship in an ER diagram.

## One-to-Many Association

One-to-Many Association: This can be directly mapped to a one-to-many relationship in an ER diagram.

## Many-to-Many Association

Many-to-Many Association: In an ER diagram, a many-to-many relationship is typically represented using an associative entity (also known as a bridge table or junction table) to break down the many-to-many relationship into two one-to-many relationships.

![[Pasted image 20240220173209.png]]

## Inheritance

### Single table inheritance

Single Table Inheritance maps all fields of all classes of an inheritance structure into a single table.
![[Pasted image 20240220171304.png]]

### Class table inheritance

Class Table Inheritance use one database table per class in the inheritance structure.
![[Pasted image 20240220171509.png]]

### Concrete table inheritance

There's a table for each concrete class in the inheritance hierarchy.
![[Pasted image 20240220171625.png]]

## Sources

- [Catalog of Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/index.html)
- [Class diagram conversion to relational model](https://stackoverflow.com/questions/47169465/class-diagram-conversion-to-relational-model-inheritance-and-a-table-for-match)
- [Mapping Object Model to Data Model](https://www.visual-paradigm.com/support/documents/vpuserguide/3563/3564/85444_mappingobjec.html)
- [Different Inheritance Strategies](https://www.visual-paradigm.com/support/documents/vpuserguide/3563/3564/85388_differentinh.html)
