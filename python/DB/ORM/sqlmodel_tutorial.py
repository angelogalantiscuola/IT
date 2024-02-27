"""
SQLModel is a library for interacting with SQL databases from Python, 
and it uses Python's type annotations to define the structure of the database tables and their relationships.
"""

from sqlmodel import Field, Session, SQLModel, create_engine, select, or_
from sqlalchemy import text


class Hero(SQLModel, table=True):
    # This line is defining a field named id that can be an integer or None.
    # The Field function is used to provide additional information about the field.
    # In this case, it's saying that the default value of id is None and that it's the primary key of the table.
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    # This line is defining a field named age that can be an integer or None. The default value of age is None.
    age: int | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


# This function returns an instance of Engine that represents the core interface to the database.
# echo=True: This is an optional parameter that sets up SQLAlchemy logging, which is useful for debugging
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    # SQLModel.metadata: This is a collection of all the Table objects you've defined in your SQLModel classes.
    # create_all(engine): This method creates all the tables stored in the metadata on the actual database.
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    # This line is creating a new Session instance associated with our database engine.
    # The with statement ensures that the Session's resources are properly released after we're done with it.
    with Session(engine) as session:
        if session.exec(select(Hero)).first() is None:  # Check if the database is empty
            session.add(hero_1)
            # equivalent to "INSERT INTO hero (name, secret_name, age) VALUES ('Deadpond', 'Dive Wilson', NULL)"
            session.add(hero_2)
            session.add(hero_3)
            session.add(hero_4)
            session.add(hero_5)
            session.add(hero_6)
            session.add(hero_7)
            # At this point, the instances are only added to the session, not yet to the database.
            # After this line is executed, the new heroes are officially in the database.
            session.commit()


def select_heroes():
    with Session(engine) as session:
        # statement = select(Hero)
        # equivalent to "SELECT * FROM hero"
        # statement = select(Hero).where(Hero.name == "Deadpond")
        # equivalent to "SELECT * FROM hero WHERE name = 'Deadpond'"
        # statement = select(Hero).where(Hero.name == "Deadpond").where(Hero.age == 48)
        # equivalent to "SELECT * FROM hero WHERE name = 'Deadpond' AND age = 48"
        # statement = select(Hero).where(Hero.age > 35)
        # equivalent to "SELECT * FROM hero WHERE age > 35"
        statement = select(Hero).where(or_(Hero.age <= 35, Hero.age > 90))
        # equivalent to "SELECT * FROM hero WHERE age <= 35 OR age > 90"
        results = session.exec(statement)
        for hero in results:
            print(hero)


def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)

        hero.age = 16
        session.add(hero)
        session.commit()

        # Refresh the 'hero' instance with its current state in the database
        session.refresh(hero)
        print("Updated hero:", hero)


def delete_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Youngster")
        results = session.exec(statement)
        hero = results.one()
        print("Hero: ", hero)

        session.delete(hero)
        session.commit()

        print("Deleted hero:", hero)

        statement = select(Hero).where(Hero.name == "Spider-Youngster")
        results = session.exec(statement)
        hero = results.first()

        if hero is None:
            print("There's no hero named Spider-Youngster")


def query_using_SQL_code(statement):
    with Session(engine) as session:
        results = session.exec(text(statement))
        for hero in results:
            print(hero)


# CRUD operations: Create, Read, Update, Delete
def create():
    create_heroes()


def read():
    select_heroes()


def update():
    update_heroes()


def delete():
    delete_heroes()


def main():
    create_db_and_tables()  # create the database and the tables
    create()  # insert data into the database
    read()  # select data from the database
    update()  # update data in the database
    delete()  # delete data from the database

    # Using SQL code
    statement = "SELECT * FROM hero WHERE age > 35"
    query_using_SQL_code(statement)


if __name__ == "__main__":
    main()
