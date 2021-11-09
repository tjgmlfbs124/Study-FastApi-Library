from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from userManager import get_user_manager
from models.User import User, UserCreate, UserUpdate, UserDB

app = FastAPI()

SECRET = "SECadRET"

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(requires_verification=False),
    prefix="/users",
    tags=["users"],
)