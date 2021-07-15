from typing import Any

from fastapi import APIRouter

from app import schemas
from app.core.celery_app import celery_app

router = APIRouter()


@router.post("/test-celery/", status_code=201)
def test_celery(
    msg: str,
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg])
    return {"msg": "Word received"}

@router.post("/info/")
def info(animal: str):
    """Returns info by animal name...it only knows kangaroo"""
    if animal == "kangaroo":
        resp = {"id":1, "name":"kangaroo", "fun_fact":"Kangaroos Are the Largest Marsupials on Earth"}
    else:
        resp = {"error": "this needs handling better"}

    return resp
