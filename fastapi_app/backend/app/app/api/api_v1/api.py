from fastapi import APIRouter

from app.api.api_v1.endpoints import utils, animals, neo4j_example

api_router = APIRouter()
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(animals.router, prefix="/animals", tags=["animals"])
api_router.include_router(neo4j_example.router, prefix="/neo4j", tags=["neo4j"])
