import unittest
import json

from flask import Flask

from app import app
from models import FilmRecord
from extensions import db


class FilmTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        db.init_app(self.app)
        self.db = db
        self.init_db()

    def init_db(self):
        films = [{"title": "Aliens",
                  "director": "Ridley Scott"}]
        with self.app.app_context():
            self.db.create_all()
            for film in films:
                self.db.session.add(FilmRecord(**film))
            self.db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()
            self.db.session.commit()

    def test_get_film_list(self):
        with self.app.test_client() as test_client:
            response = test_client.get('/api/v1/film')
        
        film = [{"id": 1,
                  "title": "Aliens",
                  "director": "Ridley Scott"}]
        
        self.assertEqual(response.json, film)
        self.assertEqual(response.status_code, 200)
    
    def test_get_film(self):
        with self.app.test_client() as test_client:
            response = test_client.get('/api/v1/film/1')
        
        film = {"id": 1,
                 "title": "Aliens",
                 "director": "Ridley Scott"}
        
        self.assertEqual(response.json, film)
        self.assertEqual(response.status_code, 200)

    def test_get_film_fail(self):
        with self.app.test_client() as test_client:
            response = test_client.get('/api/v1/film/2')

        self.assertEqual(response.json['message'], 'Could not find film_id: 2')
        self.assertEqual(response.status_code, 404)

    def test_post_film(self):
        film = {"title": "Citizen Kane",
                "director": "Orson Welles"}

        with self.app.test_client() as test_client:
            response = test_client.post('/api/v1/film',
                        headers={"Content-Type": "application/json"},
                        data=json.dumps(film))
        
        self.assertEqual(response.json['title'], film['title'])
        self.assertEqual(response.json['director'], film['director'])
        self.assertEqual(response.status_code, 201)

        with self.app.test_client() as test_client:
            response = test_client.get('/api/v1/film/2')
        
        self.assertEqual(response.json['id'], 2)
        self.assertEqual(response.json['title'], film['title'])
        self.assertEqual(response.json['director'], film['director'])
        self.assertEqual(response.status_code, 200)

    def test_delete_film(self):
        with self.app.test_client() as test_client:
            response = test_client.delete('/api/v1/film/1')

        self.assertEqual(response.json, 'Deleted Film(1, Aliens, Ridley Scott)')
        self.assertEqual(response.status_code, 200)

    def test_delete_film_fail(self):
        with self.app.test_client() as test_client:
            response = test_client.delete('/api/v1/film/2')

        self.assertEqual(response.json['message'], 'Could not find film_id: 2')
        self.assertEqual(response.status_code, 404)