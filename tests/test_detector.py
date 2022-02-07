from fastapi.testclient import TestClient
import sys

sys.path.append("..")
from src.app_heureka.main import get_app


client = TestClient(get_app)


def test_read_main():
    response = client.get("/predict-language")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
