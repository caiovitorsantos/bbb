import os, pytest

from tests.conftest import client, create_subscriber
from src.models.subscriber import Subscriber

def test_new_subscriber(create_subscriber: pytest.fixture):
    subscriber = create_subscriber

    assert subscriber.name == "Test"
    assert subscriber.email == "test@gmail.com"
    assert subscriber.youtube_url == "https://www.youtube.com/test"

def test_subscriber_to_dict(create_subscriber: pytest.fixture):
    subscriber = create_subscriber

    subscriber_dict = subscriber.to_dict()

    assert subscriber_dict['name'] == "Test"
    assert subscriber_dict['email'] == "test@gmail.com"
    assert subscriber_dict['youtube_url'] == "https://www.youtube.com/test"

def test_subscriber_from_dict():
    subscriber_dict = {
        "name": "Test",
        "email": "test@gmail.com",
        "youtube_url": "https://www.youtube.com/test"
    }

    subscriber = Subscriber.from_dict(subscriber_dict)

    assert subscriber.name == "Test"
    assert subscriber.email == "test@gmail.com"
    assert subscriber.youtube_url == "https://www.youtube.com/test"

