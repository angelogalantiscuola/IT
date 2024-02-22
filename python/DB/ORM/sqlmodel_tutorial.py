from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


def create_heroes():

    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    engine = create_engine("sqlite:///database.db", echo=True)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()


def select_heroes():
    engine = create_engine("sqlite:///database.db")

    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        hero = session.exec(statement).first()
        print(hero)


if __name__ == "__main__":
    create_heroes()
    # select_heroes()
