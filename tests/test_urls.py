from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_redirect():
    # crear
    r = client.post("/api/urls", json={"url":"https://example.com"})
    assert r.status_code == 201
    data = r.json()
    slug = data["slug"]

    # info
    r = client.get(f"/api/urls/{slug}")
    assert r.status_code == 200
    assert r.json()["clicks"] == 0

    # redirect
    r = client.get(f"/{slug}", allow_redirects=False)
    assert r.status_code in (302, 307)
