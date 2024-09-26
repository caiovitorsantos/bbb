import os
import pytest

from tests.conftest import client, create_subscriber


def test_get_all_subscribers(client, create_subscriber: pytest.fixture):
    subscriber = create_subscriber
    response = client.get('/subscribers')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == "Test"
    assert data[0]['email'] == "test@gmail.com"
    assert data[0]['youtube_url'] == "https://www.youtube.com/test"

def test_get_subscriber(client, create_subscriber: pytest.fixture):
    subscriber = create_subscriber
    response = client.get('/subscribers/1')
    data = response.get_json()

    assert response.status_code == 200
    assert data['name'] == "Test"
    assert data['email'] == "test@gmaill.com"
    assert data['youtube_url'] == "https://www.youtube.com/test"

def test_get_subscriber_not_found(client):
    response = client.get('/subscribers/1')
    data = response.get_json()

    assert response.status_code == 404
    assert data['error'] == "Subscriber not found"

def test_create_subscriber(client):
    response = client.post('/subscribers', json={
        "name": "New User",
        "email": "new_user@gmail.com",
        "youtube_url": "https://www.youtube.com/new_user"
    })

    data = response.get_json()

    assert response.status_code == 201
    assert data['message'] == "Subscriber created successfully!"

def test_create_subscriber_invalid(client):
    response = client.post('/subscribers', json={
        "name": "Test",
        "email": "test@gmail.com"
    })

    data = response.get_json()

    assert response.status_code == 422
    assert data['error'] == "Error creating subscriber"

def test_create_subscriber_missing_data(client):
    response = client.post('/subscribers', json={})
    data = response.get_json()

    assert response.status_code == 422
    assert data['error'] == "Error creating subscriber"

def test_update_subscriber(client, create_subscriber: pytest.fixture):
    subscriber = create_subscriber
    response = client.put('/subscribers/1', json={
        "name": "Test Updated",
        "email": "test@gmail.com",
        "youtube_url": "https://www.youtube.com/test"
    })

    data = response.get_json()

    assert response.status_code == 200
    assert data['message'] == "Subscriber updated successfully!"

def test_update_subscriber_not_found(client):
    response = client.put('/subscribers/1', json={
        "name": "Test Updated",
        "email": "test@gmail.com",
        "youtube_url": "https://www.youtube.com/test"
    })

    data = response.get_json()

    assert response.status_code == 404
    assert data['error'] == "Subscriber not found"

def test_update_subscriber_invalid(client, create_subscriber: pytest.fixture):
    subscriber = create_subscriber
    response = client.put('/subscribers/1', json={
        "name": "Test Updated",
        "email": "test@gmail.com",
        "youtube_url": "https://www.youtube.com/test"
    })

    data = response.get_json()

    assert response.status_code == 422
    assert data['error'] == "Error updating subscriber"

def test_update_subscriber_missing_data(client, create_subscriber: pytest.fixture):
    subscriber = create_subscriber
    response = client.put('/subscribers/1', json={})
    data = response.get_json()

    assert response.status_code == 422
    assert data['error'] == "Error updating subscriber"

def test_delete_subscriber(client, create_subscriber: pytest.fixture):
    subscriber = create_subscriber
    response = client.delete('/subscribers/1')
    data = response.get_json()

    assert response.status_code == 200
    assert data['message'] == "Subscriber deleted successfully!"

def test_delete_subscriber_not_found(client):
    response = client.delete('/subscribers/1')
    data = response.get_json()

    assert response.status_code == 404
    assert data['error'] == "Subscriber not found"

def test_delete_subscriber_invalid(client):
    response = client.delete('/subscribers/1')
    data = response.get_json()

    assert response.status_code == 422
    assert data['error'] == "Error deleting subscriber"

def test_delete_subscriber_missing_data(client):
    response = client.delete('/subscribers/1')
    data = response.get_json()

    assert response.status_code == 422
    assert data['error'] == "Error deleting subscriber"