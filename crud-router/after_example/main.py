from fastapi import FastAPI
from models import Item, UpdateItem
from dto import Item as ItemDto
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi_crudrouter import MemoryCRUDRouter

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def token_auth(token: str=Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(401, "Invalid token")


router = MemoryCRUDRouter(schema=Item, dependencies=[Depends(token_auth)])

app.include_router(router)




