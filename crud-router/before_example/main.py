from fastapi import FastAPI
from ..models import Item, UpdateItem
from ..dto import Item as ItemDto
from typing import List

app = FastAPI()

@app.get("/item/{itemId}", response_model=ItemDto, description="find One Item")
def getItem(itemId: int) -> ItemDto:

    return getItem(item_id=itemId)


@app.get("/items", response_model=List[ItemDto], description="find All by Items")
def getItems() -> List[ItemDto]:

    return getItems()


@app.post("/item", response_model=ItemDto)
def saveItem(item: Item) -> ItemDto:
    resultItem = createItem(item)

    return resultItem

@app.put("/item/{itemId}", response_model=ItemDto)
def updateItem(itemId: int, updateItem: UpdateItem):

    return updateItemById(item_id=itemId, item=updateItem)

@app.delete("/item/{itemId}", response_model=int)
def deleteItem(itemId: int):
    return deleteItemById(itemId)




def getItem(item_id: int) -> ItemDto:
    findItem = ItemDto(
        id=item_id,
        name="스텐드",
        price=30000,
        create_at="2021-12-26"
    )
    return findItem


def getItems() -> List[ItemDto]:
    findItems = []
    items = [
        [1, "컴퓨터", 1320000, "2021-12-25"],
        [2, "키보드", 58000, "2021-11-23"],
        [3, "마우스", 22000, "2021-10-09"],
        [4, "모니터", 300000, "2021-01-22"],
        [5, "마이크", 34000, "2021-03-13"]
    ]

    for item in items:
        findItems.append(
            ItemDto(
                id=item[0],
                name=item[1],
                price=item[2],
                create_at=item[3]
            )
        )

    return findItems

def createItem(item: Item):
    return item

def updateItemById(item_id: int, item: UpdateItem):
    return Item(
        id=item_id,
        item=item.name,
        price=item.price
    )

def deleteItemById(item_id: int):
    return 1