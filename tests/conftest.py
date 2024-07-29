import pytest
from mm_mongo.mongo import MongoConnection
from pymongo.database import Database


@pytest.fixture
def mongo_database() -> Database:
    conn = MongoConnection.connect("mongodb://localhost/mm-mongo-py__test")
    conn.client.drop_database(conn.database)

    conn = MongoConnection.connect("mongodb://localhost/mm-mongo-py__test")
    return conn.database
