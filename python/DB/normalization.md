# Normalization

Database normalization is a process used to organize a database into tables and columns. The main idea with this is that **a table should be about a specific topic** and only supporting topics included.

There are three main reasons to normalize a database:

1. **Minimize duplicate data**: Data duplication can lead to a lot of issues, including data anomalies, wasted storage space, and increased complexity.

2. **Minimize or avoid data modification issues**: If data is duplicated, changes need to be made in multiple places. Normalization can minimize the need for this.

3. **Simplify queries**: With data in a consistent place, queries can be simpler and more efficient.

Normalization is typically done in stages, referred to as normal forms:

- **First Normal Form (1NF)**: Data is stored in tables with rows uniquely identified by a primary key. Each column contains atomic (indivisible) values, and there are no repeating groups.

- **Second Normal Form (2NF)**: All non-key attributes are fully functional dependent on the primary key. In other words, if a table has a composite primary key (consists of two or more columns), then every non-key attribute should be dependent on the full set of primary key attributes.

- **Third Normal Form (3NF)**: All non-key attributes are not dependent on other non-key attributes. There should be no transitive dependency.

- **Boyce-Codd Normal Form (BCNF)**: A stronger version of 3NF where every determinant is a candidate key.

- **Fourth Normal Form (4NF)**: Removes multi-valued dependencies.

- **Fifth Normal Form (5NF)**: Also known as Project-Join Normal Form (PJNF), it removes dependencies resulting from joining tables to meet a user query.

Remember, normalization, while beneficial, is not always the end goal. **Sometimes, database designers denormalize certain areas for performance reasons.**

## Example

### From unnormalized to 1NF

Here's an example of a table that is not in First Normal Form (1NF):

StudentCourses Table:

| StudentID | StudentName | Courses |
|---|---|---|
| 1 | Alice | Math, Science |
| 2 | Bob | English, Math |
| 3 | Charlie | History |

This table is not in 1NF because the `Courses` column contains multiple values (Math, Science, etc.) for each row, violating the rule that each column should contain atomic (indivisible) values.

To bring this table into 1NF, we would need to ensure that each column contains only atomic values. One way to do this would be to create a new row for each course that a student is taking:

StudentCourses Table (1NF):

| StudentID | StudentName | Course |
|---|---|---|
| 1 | Alice | Math |
| 1 | Alice | Science |
| 2 | Bob | English |
| 2 | Bob | Math |
| 3 | Charlie | History |

### From 1NF to 2NF

To move from First Normal Form (1NF) to Second Normal Form (2NF), we need to ensure that all non-key attributes are fully functionally dependent on the primary key. This means that if a table has a composite primary key, then every non-key attribute should be dependent on the full set of primary key attributes.

The primary key is a composite of `StudentID` and `Course`. The non-key attribute is `StudentName`. However, `StudentName` is only dependent on part of the primary key (`StudentID`), not the full primary key (`StudentID` and `Course`). This violates the rules of 2NF.

To bring this table into 2NF, we would need to split it into two tables:

Students Table (2NF):

| StudentID | StudentName |
|---|---|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

Enrollments Table (2NF):

| StudentID | Course |
|---|---|
| 1 | Math |
| 1 | Science |
| 2 | English |
| 2 | Math |
| 3 | History |

Now, in the `Students` table, `StudentName` is fully dependent on `StudentID`. In the `Enrollments` table, there are no non-key attributes, so it is trivially in 2NF. This design also has the benefit of reducing data redundancy.

### From 2NF to 3NF

To move from Second Normal Form (2NF) to Third Normal Form (3NF), we need to ensure that all non-key attributes are not dependent on other non-key attributes. In other words, there should be no transitive dependency.

These tables are already in 3NF. In the `Students` table, `StudentName` is fully dependent on `StudentID` and there are no other non-key attributes. In the `Enrollments` table, there are no non-key attributes, so it is trivially in 3NF.

However, if there was a table where a non-key attribute was dependent on another non-key attribute, it would not be in 3NF. For example:

Courses Table (Not in 3NF):

| CourseID | CourseName | Department | DepartmentHead |
|---|---|---|---|
| Math101 | Calculus | Mathematics | Prof. Newton |
| Sci102 | Physics | Science | Prof. Einstein |

In this table, `DepartmentHead` is transitively dependent on `CourseID` through `Department`. To bring this table into 3NF, we would need to split it into two tables:

Courses Table (3NF):

| CourseID | CourseName | Department |
|---|---|---|
| Math101 | Calculus | Mathematics |
| Sci102 | Physics | Science |

Departments Table (3NF):

| Department | DepartmentHead |
|---|---|
| Mathematics | Prof. Newton |
| Science | Prof. Einstein |

Now, in both tables, all non-key attributes are fully dependent on the primary key and there are no transitive dependencies.

### From 3NF to BCNF

**Boyce-Codd Normal Form (BCNF)** is a version of the Third Normal Form (3NF) with a stronger condition. A table is in BCNF if, and only if, for every one of its dependencies X → Y, at least one of the following conditions hold:

- X is a superkey.
- Each attribute in Y-X (the set difference) is a prime attribute (i.e., each attribute in Y that is not in X is part of some candidate key).

In simpler terms, this means that for every non-trivial functional dependency (X → Y), X should be a superkey. A superkey is a set of columns such that no two rows will have the same combination of values for these columns. 

BCNF is used to prevent redundancy due to functional dependencies. A table that is in 3NF but not in BCNF is likely to have redundancy.

