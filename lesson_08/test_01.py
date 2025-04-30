
import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
API_KEY = "pDHNN61PZXEmeJnInsb-MYY5j95t4Z-7yaqKqg3YWAuOUdN7trseQ0yqXsV1k3Pd"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}


@pytest.fixture
def created_project():
    payload = {"title": "Test Project"}
    resp = requests.post(BASE_URL, json=payload, headers=HEADERS)

    if resp.status_code != 201:
        print(f"Ошибка создания проекта: {resp.json()}")
        pytest.fail("Не удалось создать проект для теста")

    project = resp.json()
    yield project

# Позитивные проверки


def test_create_project():
    payload = {"title": "New Project"}
    response = requests.post(BASE_URL, json=payload, headers=HEADERS)
    print(response.json())
    assert response.status_code == 201


def test_get_project(created_project):
    project_id = created_project["id"]
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 200


def test_update_project(created_project):
    project_id = created_project["id"]
    payload = {"title": "Updated Title"}
    response = requests.put(f"{BASE_URL}/{project_id}",
                            json=payload, headers=HEADERS)
    assert response.status_code == 200

# Негативные Проверки


def test_create_project_without_title():
    response = requests.post(BASE_URL, json={}, headers=HEADERS)
    assert response.status_code == 400


def test_update_nonexistent_project():
    response = requests.put(f"{BASE_URL}/369852000",
                            json={"title": "Test"}, headers=HEADERS)
    assert response.status_code in [400, 404]


def test_get_nonexistent_project():
    response = requests.get(f"{BASE_URL}/369852147", headers=HEADERS)
    assert response.status_code == 404
