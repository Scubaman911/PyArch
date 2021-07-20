from typing import Any

from fastapi import APIRouter

from app.core.celery_app import celery_app

router = APIRouter()


@router.post("/test-celery/", status_code=201)
def test_celery(msg: str) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg])
    return {"msg": "Word received"}
