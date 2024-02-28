from sqlmodel import Session, select, or_
from models import Hero, Team


def create_heroes_using_the_FK(engine):
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


# RA = relationship attributes
# see https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/
def create_heroes_using_the_RA(engine):
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", team=team_z_force)
        hero_rusty_man = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, team=team_preventers)
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        # we don't even have to put the teams explicitly in the session with session.add(team),
        # because these Team instances are already associated with heroes that we do add to the session.
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Created hero:", hero_deadpond)
        print("Created hero:", hero_rusty_man)
        print("Created hero:", hero_spider_boy)

        hero_spider_boy.team = team_preventers
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)
        print("Updated hero:", hero_spider_boy)

        hero_black_lion = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
        hero_sure_e = Hero(name="Princess Sure-E", secret_name="Sure-E")
        team_wakaland = Team(
            name="Wakaland",
            headquarters="Wakaland Capital City",
            heroes=[hero_black_lion, hero_sure_e],
        )
        session.add(team_wakaland)
        # Notice that, the same as before, we only have to add the Team instance to the session,
        # and because the heroes are connected to it, they will be automatically saved too when we commit.
        session.commit()
        session.refresh(team_wakaland)
        print("Team Wakaland:", team_wakaland)

        hero_tarantula = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
        hero_dr_weird = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
        hero_cap = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

        team_preventers.heroes.append(hero_tarantula)
        team_preventers.heroes.append(hero_dr_weird)
        team_preventers.heroes.append(hero_cap)
        session.add(team_preventers)
        # And in the same way as before, we don't even have to add() the independent heroes
        # to the session, because they are connected to the team.
        session.commit()
        session.refresh(hero_tarantula)
        session.refresh(hero_dr_weird)
        session.refresh(hero_cap)
        print("Preventers new hero:", hero_tarantula)
        print("Preventers new hero:", hero_dr_weird)
        print("Preventers new hero:", hero_cap)


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


def select_heroes_using_RA(engine):
    with Session(engine) as session:

        statement = select(Hero).where(Hero.name == "Spider-Boy")
        result = session.exec(statement)
        hero_spider_boy = result.one()

        # old way
        # statement = select(Team).where(Team.id == hero_spider_boy.team_id)
        # result = session.exec(statement)
        # team = result.first()
        # print("Spider-Boy's team:", team)

        # new way
        print("Spider-Boy's team again:", hero_spider_boy.team)

        # other example
        statement = select(Team).where(Team.name == "Preventers")
        result = session.exec(statement)
        team_preventers = result.one()

        print("Preventers heroes:", team_preventers.heroes)


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


def update_heroes_using_RA(engine):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        result = session.exec(statement)
        hero_spider_boy = result.one()

        hero_spider_boy.team = None
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_spider_boy)
        print("Spider-Boy without team:", hero_spider_boy)


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
