import databases
import sqlalchemy
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from db import UserDB
from typing import Optional
import datetime
from sqlalchemy.types import INT, VARCHAR, TEXT, DATETIME, FLOAT
from sqlalchemy import Column

# DATABASE_URL = "mysql+pymysql://root:emsys$$$@localhost:3306/test_alchemy"
DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)
Base: DeclarativeMeta = declarative_base()

class UserTable(Base, SQLAlchemyBaseUserTable):
    first_name = Column(TEXT, default=None)
    birthdate = Column(DATETIME, default=None)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
    # DATABASE_URL
)

Base.metadata.create_all(engine)

users = UserTable.__table__

async def get_user_db():
    yield SQLAlchemyUserDatabase(UserDB, database, users)