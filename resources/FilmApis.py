from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models import FilmRecord
from extensions import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('director', type=str)
parser.add_argument('page', type=int, default=1)


class FilmApi(Resource):
    def get(self, film_id):
        ''' Get a single film from the database '''
        return FilmRecord.serialize(
            FilmRecord.query.filter_by(id=film_id)
                .first_or_404(description=f"Could not find film_id: {film_id}")
        )

    @jwt_required
    def put(self, film_id):
        ''' Update a film already in the database '''
        args = parser.parse_args()
        film = FilmRecord.query.filter_by(id=film_id) \
                .first_or_404(description=f"Could not find film_id: {film_id}")
        film.title = args.title
        film.director = args.director
        db.session.commit()
        return f'Updated {film}', 200

    # @jwt_required
    def delete(self, film_id):
        ''' Remove a film from the database'''
        film = FilmRecord.query.filter_by(id=film_id) \
                .first_or_404(description=f"Could not find film_id: {film_id}")
        db.session.delete(film)
        db.session.commit()
        return f'Deleted {film}', 200


class FilmListApi(Resource):
    def get(self):
        '''
        Get list of films in the database

        Results are paginated (per_page=2) using optionalpage variable
          in the query string
        '''
        args = parser.parse_args()
        films = FilmRecord.query.all()
        
        # Manual Pagination
        # items_per_page = 2
        # i = (args.page - 1) * items_per_page
        # films = films[i:i + items_per_page]
        # if not films:
        #     from resources.errors import InvalidPageError
        #     raise InvalidPageError
        # return [FilmRecord.serialize(film) for film in films]
        
        films = FilmRecord.query.paginate(page=args.page,
                                          per_page=2,
                                          error_out=True)
        return [FilmRecord.serialize(film) for film in films.items]

    # @jwt_required
    def post(self):
        ''' Insert new Film with title and director '''
        args = parser.parse_args()
        new_film_record = FilmRecord(title=args.title, director=args.director)
        db.session.add(new_film_record)
        db.session.commit()
        return FilmRecord.serialize(new_film_record), 201
