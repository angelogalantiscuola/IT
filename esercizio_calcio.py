from typing import Optional
from sqlmodel import Field, Relationship, SQLModel, Session, create_engine, select

import os


class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    city: str
    players: list["Player"] = Relationship(back_populates="team")


class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surname: str
    number: int
    role: str
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="players")


# RA = relationship attributes
# see https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/
def create_records(engine):
    with Session(engine) as session:
        team_milan = Team(name="AC Milan", city="Milan")
        team_inter = Team(name="Inter", city="Milan")
        team_juve = Team(name="Juventus", city="Turin")

        player_maldini = Player(name="Paolo", surname="Maldini", number=3, role="defender", team=team_milan)
        player_zanetti = Player(name="Javier", surname="Zanetti", number=4, role="defender", team=team_inter)
        player_del_piero = Player(name="Alessandro", surname="Del Piero", number=10, role="forward", team=team_juve)
        player_pirlo = Player(name="Andrea", surname="Pirlo", number=21, role="midfielder", team=team_juve)
        player_buffon = Player(name="Gianluigi", surname="Buffon", number=1, role="goalkeeper", team=team_juve)

        session.add(player_maldini)
        session.add(player_zanetti)
        session.add(player_del_piero)
        session.add(player_pirlo)
        session.add(player_buffon)

        session.commit()

        session.refresh(player_maldini)
        session.refresh(player_zanetti)
        session.refresh(player_del_piero)
        session.refresh(player_pirlo)
        session.refresh(player_buffon)

        # print the players
        print(player_maldini)
        print(player_zanetti)
        print(player_del_piero)
        print(player_pirlo)
        print(player_buffon)


def select_records(engine):
    with Session(engine) as session:

        statement = select(Team)
        # .where(Hero.name == "Spider-Boy")
        result = session.exec(statement)

        # print all records
        for team in result:
            print(team)
            print(team.players)

        # # new way
        # print("Spider-Boy's team again:", hero_spider_boy.team)

        # # other example
        # statement = select(Team).where(Team.name == "Preventers")
        # result = session.exec(statement)
        # team_preventers = result.one()

        # print("Preventers heroes:", team_preventers.heroes)


def create_engine_with_db(db_name: str, echo: bool):
    sqlite_url = f"sqlite:///{db_name}"
    return create_engine(sqlite_url, echo=echo)


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def main():
    db_name = "teams.db"
    verbose = False
    delete_database = True
    if delete_database:
        try:
            os.remove(db_name)
        except FileNotFoundError:
            print(f"{db_name} not found")
            exit()
    engine = create_engine_with_db(db_name, verbose)
    create_db_and_tables(engine)
    create_records(engine)
    select_records(engine)
    # update_heroes(engine)
    # delete_heroes(engine)


if __name__ == "__main__":
    main()
