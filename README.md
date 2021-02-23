# Film Database API
This is a Toy API I was building in my own time. The goal of this Toy API was to create a project beyond simply using raw Flask alone. I was inspired by a [guide](https://dev.to/paurakhsharma/series/3672) but took some liberties with it like using SQL instead of MongoDB.

I was able utilize the Flask-RESTful package, Flask-SQLAlchemy and SQlite for the ORM, add user sign up and functionality with Flask-bcrypt and Flask-JWT-Extended, and some unit tests.

Functions surrounding the Film portion of the database is more or less fully realized. The portions regarding sign up and login are functional although mostly disabled by commenting out the `@jwt_required` simply because it was not something I wanted to handle while creating the unit tests.


### Run Init DB
python init_db.py

### Tests
```
ENV_FILE_LOCATION=tests/.env.test python3 -m unittest
```

Importing is a lingering issue. Tests must be run from the root of the folder as in the command above.

Tests are not mocked. The test class will set up a (smaller) real DB called `test.db`, though in this case, nearly identical to the production db since there are only a few data points. Database initialization 

Tests are incomplete. There are currently no tests for anything related to Users, login, authentication nor authorization.
