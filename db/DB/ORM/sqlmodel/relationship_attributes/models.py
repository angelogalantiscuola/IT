from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # to find out more about indexes in SQLModel, check the documentation
    # https://sqlmodel.tiangolo.com/tutorial/indexes/
    name: str = Field(index=True)
    headquarters: str
    # Why the "" around "Hero"?
    # https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/type-annotation-strings/
    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    team_id: int | None = Field(default=None, foreign_key="team.id")

    # These new attributes are not the same as fields,
    # they don't represent a column directly in the database,
    # and their value is not a singular value like an integer.
    # Their value is the actual entire object that is related.
    team: Team | None = Relationship(back_populates="heroes")
