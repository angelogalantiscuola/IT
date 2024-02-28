from sqlmodel import Session, select
from models import Hero, Team


def create_heroes(engine):
    # This line is creating a new Session instance associated with our database engine.
    # The with statement ensures that the Session's resources are properly released after we're done with it.
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")
        session.add(team_preventers)
        session.add(team_z_force)
        session.commit()

        hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", team_id=team_z_force.id)
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            team_id=team_preventers.id,
        )
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        # At this point, the instances are only added to the session, not yet to the database.
        # After this line is executed, the new heroes are officially in the database.
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Created hero:", hero_deadpond)
        print("Created hero:", hero_rusty_man)
        print("Created hero:", hero_spider_boy)


def select_heroes(engine):
    with Session(engine) as session:
        # statement = select(Hero)
        # equivalent to "SELECT * FROM hero"

        # statement = select(Hero).where(Hero.name == "Deadpond").where(Hero.age == 48)
        # equivalent to "SELECT * FROM hero WHERE name = 'Deadpond' AND age = 48"

        # results = session.exec(statement)
        # for hero in results:
        #     print(hero)

        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        # # Alternatively, use the join method to join the Hero and Team tables.
        # statement = select(Hero, Team).join(Team)
        # # Or outer join to include heroes without a team.
        # statement = select(Hero, Team).join(Team, isouter=True)
        print("-" * 50)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)
        print("-" * 50)


def update_heroes(engine):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero_1 = results.one()
        print("Hero 1:", hero_1)

        hero_1.age = 16
        hero_1.name = "Spider-Youngster"
        session.add(hero_1)

        session.commit()
        session.refresh(hero_1)

        print("Updated hero 1:", hero_1)


def delete_heroes(engine):
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
