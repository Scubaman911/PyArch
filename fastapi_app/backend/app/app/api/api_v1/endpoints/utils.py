from typing import Any

from fastapi import APIRouter
import pika

from app.core.celery_app import celery_app

router = APIRouter()


@router.post("/test-celery/", status_code=201)
def test_celery(msg: str) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg])
    return {"msg": "Word received"}


@router.post("/send-msg", status_code=201)
def send_msg(msg: str) -> Any:
    """
    Send RabbitMQ message
    """
    urlparams = pika.URLParameters('amqp://queue')
    connection = pika.BlockingConnection(urlparams)
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
    routing_key='hello',
    body='hello world!')

    print(" [x] Sent 'Hello World!'")
    connection.close()