import os, pytest
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from main import app, db
from src.models.subscriber import Subscriber

app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

@pytest.fixture(scope='module')
def create_subscriber():
    subscriber = Subscriber(
        subscriber_id=None,
        name="Test",
        email="test@gmail.com",
        youtube_url="https://www.youtube.com/test"
    )

    db.session.add(subscriber)
    db.session.commit()

    return subscriber
