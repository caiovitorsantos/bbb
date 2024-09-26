from src.models.subscriber import Subscriber
from src.adapters.db_adapter import DbAdapter
import json

class SubscriberRepository:
    def __init__(self, db_adapter=DbAdapter()):
        db_adapter.create_connection()
        self.db = db_adapter
    
    def get_all(self):
        query = "SELECT * FROM subscribers"
        result = self.db.execute_query(query)

        return self.__build_subscriber_list(result)

    def get_by_id(self, subscriber_id):
        query = "SELECT * FROM subscribers WHERE subscriber_id = %s"
        params = (subscriber_id,)

        result = self.db.execute_query(query, params)

        if not result:
            return None

        return Subscriber(
            subscriber_id=result[0]['subscriber_id'],
            name=result[0]['name'],
            email=result[0]['email'],
            youtube_url=result[0]['youtube_url']
        ).to_dict()
    
    def create(self, subscriber):
        query = "INSERT INTO subscribers (name, email, youtube_url) VALUES (%s, %s, %s)"
        params = (subscriber['name'], subscriber['email'], subscriber['youtube_url'])
        result = self.db.execute_command(query, params)

        return result
    
    def update(self, subscriber_id, subscriber_data):
        query = "UPDATE subscribers SET name = %s, email = %s, youtube_url = %s WHERE subscriber_id = %s"
        params = (subscriber_data['name'], subscriber_data['email'], subscriber_data['youtube_url'], subscriber_id)
        subscriber = self.db.execute_command(query, params)

        return subscriber
    
    def delete(self, subscriber_id):
        query = "DELETE FROM subscribers WHERE subscriber_id = %s"
        params = (subscriber_id,)
        subscriber = self.db.execute_command(query, params)
        return subscriber
    
    def __build_subscriber_list(self, result):
        subscriber_list = []

        for row in result:
            subscriber = Subscriber(
                subscriber_id=row['subscriber_id'],
                name=row['name'],
                email=row['email'],
                youtube_url=row['youtube_url']
            )
            subscriber_list.append(subscriber.to_dict())

        return subscriber_list