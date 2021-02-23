import datetime

from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from extensions import db
from models import UserRecord
from resources.errors import (UnauthorizedError,
                              EmailAlreadyExistsError,
                              UsernameAlreadyExistsError)


parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class SignupApi(Resource):
    def post(self):
        '''
        Create a new user in the database with email, username, and password
        '''
        args = parser.parse_args()
        user = UserRecord(email=args.email,
                          username=args.username,
                          password=args.password)
        user.hash_password()

        if UserRecord.query.filter_by(email=args.email).first():
            raise EmailAlreadyExistsError
        if UserRecord.query.filter_by(username=args.username).first():
            raise UsernameAlreadyExistsError

        db.session.add(user)
        db.session.commit()
        return f"Added {user}", 200

class LoginApi(Resource):
    def get(self):
        '''
        Get all users in the database

        Primarily an endpoint for testing the signup
        '''
        return [user.serialize() for user in UserRecord.query.all()]

    def post(self):
        '''
        Post email and password to receive a new access token
          for methods that require authorization
        '''
        args = parser.parse_args()
        email = args.email
        user = UserRecord.query.filter_by(email=email) \
                .first_or_404(description=f"Could not find user email {email} ")
        authorized = user.check_password(args.password)
        if not authorized:
            return UnauthorizedError
        
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id),
                                           expires_delta=expires)
        return {'token': access_token}, 200
