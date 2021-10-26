from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model.farm import Farm
from db.databases import get_db
from pydantic import BaseModel
from fastapi_crudrouter import SQLAlchemyCRUDRouter

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:emsys1001@localhost:3306/lab"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)

class PotatoCreate(BaseModel):
    thickness: float
    mass: float
    color: str
    type: str

router = SQLAlchemyCRUDRouter(
    schema=Farm,
    create_schema=Farm,
    db_model=Farm,
    db=get_db,
    prefix='potato'
)

app.include_router(router)