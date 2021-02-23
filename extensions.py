from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


db = SQLAlchemy()
api = Api()
bcrypt = Bcrypt()
jwt = JWTManager()
