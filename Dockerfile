FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN python -m venv env
RUN . env/bin/activate

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN pip install poetry
RUN poetry install

RUN poetry add flask flask-jsonpify flask-sqlalchemy flask-restful flask-cors flask-migrate pytest psycopg2
# RUN poetry run flask --app=main.py db init
# RUN poetry run flask --app=main.py db migrate

EXPOSE 5005

CMD ["poetry", "run", "flask", "run", "--port=5005", "--host=0.0.0.0", "--debug", "--reload"]
