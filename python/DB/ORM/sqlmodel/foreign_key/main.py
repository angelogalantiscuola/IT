import os
from database import create_db_and_tables, create_engine_with_db
from crud import (
    create_heroes,
    select_heroes,
    update_heroes,
    delete_heroes,
)


def main():
    db_name = "database.db"
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
    create_heroes(engine)
    select_heroes(engine)
    update_heroes(engine)
    delete_heroes(engine)


if __name__ == "__main__":
    main()
