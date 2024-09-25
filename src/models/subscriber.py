from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('/app/config.py')
db = SQLAlchemy(app)

class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    subscriber_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    youtube_url = db.Column(db.String(256), nullable=False, unique=True)

    def __init__(self, subscriber_id, name, email, youtube_url):
        self.subscriber_id = subscriber_id
        self.name = name
        self.email = email
        self.youtube_url = youtube_url

    def __repr__(self):
        return f'<Subscriber {self.name}>'

    def to_dict(self):
        return {
            'subscriber_id': self.subscriber_id,
            'name': self.name,
            'email': self.email,
            'youtube_url': self.youtube_url
        }
