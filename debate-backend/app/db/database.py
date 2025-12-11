from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL ="postgresql://postgres:password@localhost/debate_db"

engine=create_engine(DATABASE_URL)

session=sessionmaker(bind=engine,autoflush=False,autocommit=False)

base=declarative_base()
