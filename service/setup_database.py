from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
# from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    username = Column(String(80),nullable=False, unique=True)
    password_hash = Column(String(80))
    picture = Column(String(80))
    email = Column(String(100), nullable=False)

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')

    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def verify_password(self,password):
    #     return check_password_hash(self.password_hash, password)

    # @property
    # def serialize(self):
    #     """Return object data in easily serializeable format"""
    #     return json.dumps({
    #         "name": self.name,
    #         "id": self.id,
    #         "username": self.username,
    #         "picture": self.picture,
    #         "email": self.email
    #     })  


#database_url = 'postgresql://couchmaster:Welcome12#@couchbumsdb-dev.cyrebkvrvdix.us-east-1.rds.amazonaws.com:5432/couchbums'
database_url = 'mysql+mysqlconnector://couchmaster:password@couchbums-dev-db.cyrebkvrvdix.us-east-1.rds.amazonaws.com:3306/couchbums'
engine = create_engine(database_url)

Base.metadata.create_all(engine)


