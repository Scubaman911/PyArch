from time import sleep

from app.core.celery_app import celery_app


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    sleep(5)
    return f"test task return {word}"
