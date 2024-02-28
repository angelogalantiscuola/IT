from sqlmodel import SQLModel, create_engine


def create_engine_with_db(db_name: str, echo: bool):
    sqlite_url = f"sqlite:///{db_name}"
    return create_engine(sqlite_url, echo=echo)


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
