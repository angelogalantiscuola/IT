## SQLAlchemy

SQLAlchemy: SQLAlchemy is a SQL toolkit and ORM that provides a full suite of well known enterprise-level persistence patterns. It allows you to work with relational databases in Python in a way that fits with the language's idiomatic style. SQLAlchemy models can be used to automatically create, read, update, and delete records in your database using simple Python code.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

SQLAlchemy provides two ways to query your data:

SQL Expression Language: This is a comprehensive SQL abstraction toolkit that exposes the full range of SQL capabilities using Pythonic syntax. It allows you to write SQL queries using Python constructs.

ORM API: This provides a high-level, Pythonic interface for querying your data. It allows you to use Python classes and methods to query your data instead of writing SQL.

Here's an example of querying data using the ORM API:

```python
users = session.query(User).filter(User.name == 'John').all()
```

The SQL Expression Language is a part of SQLAlchemy that provides a SQL-like way to interact with your database using Python code. It's a way to build SQL statements using Python expressions. Here's an example:

```python
from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine('sqlite:///example.db')  # Use your database connection string
metadata = MetaData()

# Reflect the users table from the database
users = Table('users', metadata, autoload_with=engine)

# Build a SELECT statement
stmt = select(users).where(users.c.name == 'John')

# Execute the statement
with engine.connect() as connection:
    result = connection.execute(stmt)
    for row in result:
        print(row)
```

Yes, you can execute raw SQL queries in Python. This can be done using various database libraries, such as sqlite3 for SQLite databases, psycopg2 for PostgreSQL databases, or mysql-connector-python for MySQL databases. Here's an example using sqlite3:

```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()

# Write your SQL query
sql_query = "SELECT * FROM users WHERE name = 'John';"

# Execute the SQL query
cur.execute(sql_query)

# Fetch all the rows
rows = cur.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
```

## give me a complete hello world example of SQLAlchemy ORM

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the base model
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create the engine
engine = create_engine('sqlite:///example.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create a new session
session = Session()

# Create a new user
new_user = User(name='Hello, World!')

# Add the new user to the session
session.add(new_user)

# Commit the session
session.commit()

# Query the user
user = session.query(User).filter_by(name='Hello, World!').first()

# Print the user's name
print(user.name)

# Close the session
session.close()
```
