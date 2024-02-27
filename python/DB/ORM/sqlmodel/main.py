from database import create_db_and_tables, create_engine_with_db
from crud import create_heroes, select_heroes, update_heroes, delete_heroes


def main():
    db_name = "database.db"
    verbose = False
    engine = create_engine_with_db(db_name, verbose)
    create_db_and_tables(engine)
    create_heroes(engine)
    select_heroes(engine)
    update_heroes(engine)
    delete_heroes(engine)


if __name__ == "__main__":
    main()
