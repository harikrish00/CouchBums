from service.setup_database import Base, User
from sqlalchemy import create_engine, exists    
from sqlalchemy.orm import sessionmaker
import json
from service.jsonencoder import AlchemyEncoder
from utils.db_connection_factory import SQLAlchemyDBConnection
# from contextlib import contextmanager
import os

db_username = os.environ.get('DB_USER_NAME')
db_password = os.environ.get('DB_PASSWORD')
database_url = "mysql+mysqlconnector://{}:{}@couchbums-dev-db.cyrebkvrvdix.us-east-1.rds.amazonaws.com:3306/couchbums".format(db_username, db_password)

# @contextmanager
# def db_context_factory():
#     # database_url = os.environ.get('DATABASE_URL') or 'sqlite:///itemcatalog.db'
#     database_url = "mysql+mysqlconnector://couchmaster:password@couchbums-dev-db.cyrebkvrvdix.us-east-1.rds.amazonaws.com:3306/couchbums"
#     engine = create_engine(database_url)
#     Base.metadata.bind = engine
#     DBSession = sessionmaker(bind = engine)

#     return DBSession()


def get_user(event, context):
    with SQLAlchemyDBConnection(database_url) as db:
        users = db.session.query(User).all()
        usersJSON = json.dumps(users, cls=AlchemyEncoder)
        response = {
            "statusCode": 200,
            "body": usersJSON
        }
        return response

def create_user(event, context):
    data = json.loads(event['body'])
    newUser = User(name=data['username'],
                username=data['name'],
                email=data['email'],
                picture=data['picture'],
                password_hash=data['password_hash'],
                id=data['id'])
    with SQLAlchemyDBConnection(database_url) as db:
        db.session.add(newUser)
        db.session.commit()

    response = {
        "statusCode": 200,
    }

    return response