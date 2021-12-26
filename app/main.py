from typing import Optional
from fastapi import FastAPI
from dto import Item


app = FastAPI()

# CRUD Router

@app.get("/item", responses=)
@app.get("/items")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}