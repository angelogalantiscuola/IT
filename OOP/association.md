
## Main elements of a class diagram

In a UML (Unified Modeling Language) class diagram, you can use the following main elements:

- `Classes`: These are represented as rectangles divided into three parts: the top part contains the class name, the middle part contains the attributes of the class, and the bottom part contains the methods or operations that the class can perform.

- `Associations`: These are represented as lines connecting classes, indicating a relationship between them. The multiplicity (one, many, etc.) can be indicated at each end of the line.

- Generalizations (`Inheritance`): These are represented as hollow arrowheads pointing from a subclass to a superclass, indicating that the subclass is a type of the superclass.

## Relationships between classes

- Extension (`Inheritance`): This is represented by `<|--`. The arrow points from the subclass to the superclass.

```plantuml
@startuml
class Superclass {
}

class Subclass {
}

Subclass <|-- Superclass
@enduml
```

- An Association represents a "using" relationship between two or more classes. It is a structural relationship, in that it specifies that objects of one class are connected to objects of another and does not represent behaviour. In the context of PlantUML and UML diagrams, the `--` symbol is used to denote an association relationship between two classes.

```plantuml
@startuml
class Class1 {
}

class Class2 {
}

Class1 -- Class2
@enduml
```

## Associations in UML

### Association 1-1
1-1 Association: a User has one Profile in a system. This is a 1-1 association because each user has exactly one profile, and each profile belongs to exactly one user.

```plantuml
@startuml
class User {
  -username: String
}

class Profile {
  -bio: String
}

User "1" -- "1" Profile: has
@enduml
```

### Association 1-*
1-* Association: A Mother has Children. In this case, one mother can have zero or more children, but each child has exactly one biological mother.

```plantuml
@startuml
class Mother {
  -name: String
}

class Child {
  -name: String
}

Mother "1" -- "0..*" Child: has
@enduml
```

### Association \*-\*
\*-\* Association: A Student takes Courses. In this case, one student can take multiple courses, and each course can have multiple students.

```plantuml
@startuml
class Student {
  -name: String
}

class Course {
  -name: String
}

Student "*" -- "*" Course: takes
@enduml
```


## Associations in Python

### Association 1-*

```python
class User:
  def __init__(self, username):
    self.username = username
    self.profile = Profile(self)

class Profile:
  def __init__(self, user):
    self.bio = ""
    self.user = user
```

### Association 1-*

```python
class Mother:
  def __init__(self, name):
    self.name = name
    self.children = []

  def add_child(self, child):
    self.children.append(child)

class Child:
  def __init__(self, name):
    self.name = name
```


### Association \*-\*

```python
class Student:
  def __init__(self, name):
    self.name = name
    self.courses = []

  def take_course(self, course):
    self.courses.append(course)
    course.students.append(self)

class Course:
  def __init__(self, name):
    self.name = name
    self.students = []
```
