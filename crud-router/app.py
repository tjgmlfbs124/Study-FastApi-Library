from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter


class Potato(BaseModel):
    id: int
    color: str
    mass: float

class Item(BaseModel):
    id: int
    color: str
    mass: float


app = FastAPI()

app.include_router(CRUDRouter(schema=Potato))
app.include_router(CRUDRouter(schema=Item))
