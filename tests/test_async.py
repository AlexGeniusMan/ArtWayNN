import base64
import pytest

from httpx import AsyncClient

from app.main import app


def get_base64_str(path: str):
    with open(path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode("utf-8")
    return base64_str


@pytest.mark.asyncio
async def test_first_label():
    base64_str = get_base64_str("icons/1 — Test.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 1


@pytest.mark.asyncio
async def test_second_label():
    base64_str = get_base64_str("icons/2 — Medal.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 2


@pytest.mark.asyncio
async def test_third_label():
    base64_str = get_base64_str("icons/3 — PC.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 3


@pytest.mark.asyncio
async def test_fourth_label():
    base64_str = get_base64_str("icons/4 — Search.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 4


@pytest.mark.asyncio
async def test_fifth_label():
    base64_str = get_base64_str("icons/5 — Projector.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 5


@pytest.mark.asyncio
async def test_sixth_label():
    base64_str = get_base64_str("icons/6 — Idea.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 6


@pytest.mark.asyncio
async def test_seventh_label():
    base64_str = get_base64_str("icons/7 — Telescope.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 7


@pytest.mark.asyncio
async def test_eighth_label():
    base64_str = get_base64_str("icons/8 — Briefcase.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 8


@pytest.mark.asyncio
async def test_ninth_label():
    base64_str = get_base64_str("icons/9 — Trofy.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 9


@pytest.mark.asyncio
async def test_tenth_label():
    base64_str = get_base64_str("icons/10 — Cap.png")
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.post("/predict/", json={"base64_str": base64_str})
    assert response.status_code == 200
    
    preds = response.json()
    label = preds.index(max(preds))
    assert label+1 == 10
