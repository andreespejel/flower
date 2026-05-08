from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load variables from .env into sys environment
load_dotenv()
# acces database url via variable that was loaded
db_url = os.getenv("DATABASE_URL")

# create engine to store data in postgres directory
# (path in .env file)
engine = create_engine(db_url)

# create declarative base class
Base = declarative_base()

# create (single)table in the engine
Base.metadata.create_all(engine)

# create a session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)