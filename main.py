import logging
import sys

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.controllers.subscribers_controller import Subscribers, SubscriberById


app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

app.config.from_pyfile('config.py')
app.logging = logging

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Subscribers, '/subscribers')
api.add_resource(SubscriberById, '/subscribers/<subscriber_id>')

@app.route("/")
def hello_world():
    return {"title": "Bem vindo ao BBB!"}

if __name__ == "__main__":
    app.run(port=5005)
