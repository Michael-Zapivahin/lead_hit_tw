from fastapi.testclient import TestClient

from main import app

from tests.test_data import test_data, test_data_error, test_data_not_find


client = TestClient(app)


def test_read_main():
    headers = {'content-type': 'application/json'}
    url = "http://127.0.0.1:8000/get_form"
    response = client.post(url, headers=headers, json=test_data)
    assert response.status_code == 200
    assert response.json() == 'lk'


def test_read_main_not_find():
    headers = {'content-type': 'application/json'}
    url = "http://127.0.0.1:8000/get_form"
    response = client.post(url, headers=headers, json=test_data_not_find)
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'phone_work'


def test_read_main_error():
    headers = {'content-type': 'application/json'}
    url = "http://127.0.0.1:8000/get_form"
    response = client.post(url, headers=headers, json=test_data_error)
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'phone'



