from flask import Flask


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    register_api(app)
    return app


def register_extensions(app):
    from extensions import bcrypt, db, jwt
    
    app.config.from_envvar('ENV_FILE_LOCATION')
    
    bcrypt.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    

def register_api(app):
    from extensions import api
    from resources import FilmApi, FilmListApi, SignupApi, LoginApi
    from resources.errors import errors
    
    api.errors = errors
    api.add_resource(FilmApi, '/api/v1/film/<int:film_id>')
    api.add_resource(FilmListApi, '/api/v1/film')
    api.add_resource(SignupApi, '/api/v1/signup')
    api.add_resource(LoginApi, '/api/v1/login')
    api.init_app(app)


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
