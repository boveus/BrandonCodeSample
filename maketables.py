from sqlalchemy import Column, Integer, String, Binary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

engine = create_engine('sqlite:///user.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(Binary(60), nullable=False)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)


Base.metadata.create_all(engine)