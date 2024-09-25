
from flask import jsonify, request
from flask_restful import Resource
from sqlalchemy import create_engine

from src.repositories.subscriber_repository import SubscriberRepository
from src.models.subscriber import Subscriber


class Subscribers(Resource):
    def get(self):
        subscribers = SubscriberRepository().get_all()
        return jsonify(subscribers)

    def post(self):
        try:
            subscriber = SubscriberRepository().create(self.__post_params())

            if subscriber is True:
                return {"message": "Subscriber created successfully!"}, 201
            else:
                return {"error": "Error creating subscriber"}, 422
        except Exception as e:
            return {"error": str(e)}, 500

    def __post_params(self):
        return {
            key: request.json.get(key)
            for key in ['name', 'email', 'youtube_url']
        }


class SubscriberById(Resource):
    def get(self, subscriber_id):
        subscriber = SubscriberRepository().get_by_id(subscriber_id)
        
        if subscriber is None:
            return {"error": "Subscriber not found"}, 404
        else:
            return subscriber, 200

    def put(self, subscriber_id):
        subscriber_data = self.__put_params()
        subscriber = SubscriberRepository().update(subscriber_id, subscriber_data)

        if subscriber is True:
            return {"message": "Subscriber updated successfully!"}, 200
        else:
            return {"error": "Error updating subscriber"}, 422
    
    def delete(self, subscriber_id):
        subscriber = SubscriberRepository().delete(subscriber_id)

        if subscriber is True:
            return {"message": "Subscriber deleted successfully!"}, 200
        else:
            return {"error": "Error deleting subscriber"}, 422
    
    def __put_params(self):
        return {
            key: request.json.get(key)
            for key in ['name', 'email', 'youtube_url']
        }
        