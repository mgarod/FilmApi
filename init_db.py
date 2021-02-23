from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import FilmRecord, UserRecord
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///film.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()

films = [
    {
        "id": 1,
        "title": "Aliens",
        "director": "Ridley Scott"
    },
    {
        "id": 2,
        "title": "Citizen Kane",
        "director": "Orson Welles"
    },
    {
        "id": 3,
        "title": "Psycho",
        "director": "Alfred Hitchcock"
    },
    {
        "id": 4,
        "title": "Star Wars",
        "director": "George Lucas"
    },
    {
        "id": 5,
        "title": "The Shining",
        "director": "Stanley Kubrick"
    }
]

users = [
    {
        "id" : 1,
        "email": "test@test.com",
        "username": "NyanCat",
        "password": '12345'
    },
    {
        "id" : 2,
        "email": "a@a.com",
        "username": "ILikeTurtles",
        "password": '54321'
    }
]

with app.app_context():
    db.create_all()
    
    for film in films:
        db.session.add(FilmRecord(**film))

    for user in users:
        user_record = UserRecord(**user)
        user_record.hash_password()
        db.session.add(user_record)

    db.session.commit()