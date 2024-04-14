from fastapi.testclient import TestClient;
from main import app;

client = TestClient(app);

def test_create_message():
    response = client.post("/message", json={"message": "hello"});
    assert response.status_code == 200;
    assert response.json() == {"message": "hello"};