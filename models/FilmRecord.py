from flask_sqlalchemy import SQLAlchemy
from extensions import db


class FilmRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Film({self.id}, {self.title}, {self.director})'

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
        }
