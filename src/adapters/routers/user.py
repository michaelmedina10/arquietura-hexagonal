import json

from fastapi import APIRouter, Body, Query, Request
from fastapi.responses import JSONResponse

from application.user_handler import UserHandler
from domain.core.repositories import UserRepository

PREFIX = "/api/v1"
TAGS = ["Usuarios"]
SCHEMA = True

router = APIRouter(prefix=PREFIX, tags=TAGS, include_in_schema=SCHEMA)


@router.get("/usuarios", response_class=JSONResponse)
def get_users(request: Request, filter_query=Query("{}")):
    user_handler = UserHandler(user_repository=UserRepository())
    users = user_handler.find(filter_query=json.loads(filter_query))
    return users


@router.post("/usuarios", response_class=JSONResponse)
def post_users(request: Request, user=Body({})):
    user_handler = UserHandler(user_repository=UserRepository())
    return user_handler.insert_one(user)
