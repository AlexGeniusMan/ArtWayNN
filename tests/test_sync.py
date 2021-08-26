import base64

from fastapi.testclient import TestClient

from main import app


client = TestClient(app, base_url="http://localhost")


def get_base64_str(path: str):
    with open(path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode("utf-8")
    return base64_str


def test_first_label():
    base64_str = get_base64_str("icons/1 — Test.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 1


def test_second_label():
    base64_str = get_base64_str("icons/2 — Medal.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 2


def test_third_label():
    base64_str = get_base64_str("icons/3 — PC.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 3


def test_fourth_label():
    base64_str = get_base64_str("icons/4 — Search.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 4


def test_fifth_label():
    base64_str = get_base64_str("icons/5 — Projector.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 5


def test_sixth_label():
    base64_str = get_base64_str("icons/6 — Idea.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 6


def test_seventh_label():
    base64_str = get_base64_str("icons/7 — Telescope.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 7


def test_eighth_label():
    base64_str = get_base64_str("icons/8 — Briefcase.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 8


def test_ninth_label():
    base64_str = get_base64_str("icons/9 — Trofy.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 9


def test_tenth_label():
    base64_str = get_base64_str("icons/10 — Cap.png")
    response = client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 10
