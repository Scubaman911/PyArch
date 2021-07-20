from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def test_celery_worker_test(
    client: TestClient
) -> None:
    r = client.post(
        f"{settings.API_V1_STR}/utils/test-celery/?msg=test",
    )
    response = r.json()
    assert response["msg"] == "Word received"
