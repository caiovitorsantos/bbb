import psycopg2
from psycopg2 import Error
import logging


class DbAdapter:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, db_url='postgresql://postgres:password@db:5432/bbb'):
        self.db_url = db_url
        self.conn = None

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(self.db_url)
            logging.info(f"DbAdapter: Connection established with the database: {self.db_url}")
        except Error as e:
            logging.error(f"DbAdapter: Error connecting to the database: {e}")

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Error as e:
            logging.error(f"DbAdapter: Error executing the query: %{e}")
            return None
        finally:
            cursor.close()
            self.close_connection()

    def execute_command(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            self.conn.commit()

            return True
        except Error as e:
            logging.error(f"DbAdapter: Error executing the command: %{e}")
            return None
        finally:
            cursor.close()
            self.close_connection()

    def close_connection(self):
        if self.conn:
            self.conn.close()
            logging.info("DbAdapter: Connection to the database closed.")
