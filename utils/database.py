from sqlmodel import create_engine, Session, SQLModel

db_url = "postgresql://postgres:postgres@localhost:5432/shift_manager"
engine = create_engine(db_url, echo=True)

def init_db():
        try:
            SQLModel.metadata.create_all(engine)
        except Exception as err:
            print(err)
            exit(0)

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as err:
        print(err)
        exit(0)

