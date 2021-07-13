from app.core.celery_app import celery_app
from time import sleep

@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    sleep(5)
    return f"test task return {word}"
