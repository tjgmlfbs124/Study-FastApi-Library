from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: int
    create_at: str

class UpdateItem(BaseModel):
    name: str
    price: int