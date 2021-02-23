# Film Database API
This is a Toy API I was building in my own time. The goal of this Toy API was to create a project beyond simply using raw Flask alone. I was inspired by a [guide](https://dev.to/paurakhsharma/series/3672) but took some liberties with it like using SQL instead of MongoDB.

I was able utilize the `Flask-RESTful` package, `Flask-SQLAlchemy` and SQlite for the ORM, add user sign up and login with `Flask-bcrypt` and `Flask-JWT-Extended`, and add some unit tests using the standard library `unittest`.

Functions surrounding the Film portion of the database is more or less fully realized. The portions regarding sign up and login are functional although enforcement is mostly disabled. The enforcment was commented out (`@jwt_required`) because I did not want to have to log in while running the unit tests. This is something I would address in the future.

### Setup
Create a virtual environment and install libraries with `pip install -r requirements`

Prior to running the API, please run `python init_db.py` to create and enter dummy data into the database

Below are the included database tables and their schemas:
```sql
CREATE TABLE film_record (
        id INTEGER NOT NULL,
        title VARCHAR NOT NULL,
        director VARCHAR NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE user_record (
        id INTEGER NOT NULL,
        email VARCHAR NOT NULL,
        username VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (email),
        UNIQUE (username)
);
```

### API
Run with `ENV_FILE_LOCATION=.env python app.py`

/api/v1/film
- GET: List of all films in the database (2 per page)
    - e.g. `curl -X GET localhost:5000/api/v1/film`
    - e.g. `curl -X GET localhost:5000/api/v1/film?page=3`
- POST: Insert a film
    - e.g. `curl -X POST localhost:5000/api/v1/film -X POST -d title=Batman -d director=Tim Burton`
    - e.g. `curl -X POST "localhost:5000/api/v1/film?title=Batman&director=Tim%20Burton"`

/api/v1/film/<int:film_id>
- GET: A single film with a specific film_id
    - e.g. `curl -X GET localhost:5000/api/v1/film/3`
- PUT: Update a single film with a new title and or director
    - e.g. `curl -X PUT localhost:5000/api/v1/film/3 -d title="The Birds"`
    - e.g. `curl -X PUT "localhost:5000/api/v1/film/3?title=When%20Harry%20Met%20Sally...&director=Rob%20Reiner"`
- DELETE: Remove a single film from the database
    - e.g. `curl -X DELETE localhost:5000/api/v1/film/5`

/api/v1/signup
- POST: Create a new user in the database
    - e.g. `curl -X POST localhost:5000/api/v1/signup -d email=abc -d username=def -d password=123`
    - e.g. `curl -X POST "localhost:5000/api/v1/signup?email=abc&username=def&password=123"`

/api/v1/login
- GET: List all users in the database (meant for debugging)
    - e.g. `curl -X POST localhost:5000/api/v1/signup`
- POST: Give email and password to recieve a token endpoints requiring write-access like insert, update, and delete
    - e.g. `curl -X POST localhost:5000/api/v1/login -d email=abc -d password=123`

### Tests
```
ENV_FILE_LOCATION=tests/.env.test python3 -m unittest
```

There are some issues regarding relative imports. As such, tests are required to be run from the root of the project, and point 

Database calls are not mocked. The test class will set up a real DB called `test.db` with just 1 film record.

Database initialization happens in `setUp` which likely should be done with `setUpClass` to only run `init_db()` once per class, not every `test_*` method.

Test coverage is incomplete. There are currently no tests for anything related to Users, login, authentication nor authorization.


### Other Issues
The .env files in this project should not be included in the repository because they contain secrets. Exclusion would normally be enforced by the `.gitignore` file. For the purpose of simplicity in this project, they are added here and removed from the `.gitignore` file.

The included  signup and login functionality is no doubt insecure. Something more robust should be implemented.

There is very little manual handling for bad calls, bad data, incomplete calls, etc. Since I intended this to be a toy project, this was not my focus. However, the libraries used in this project do cover a fair deal. For example, `RequestParser` has some type enforcement for request data, and I did utilize `first_or_404` with `SQLAlchemy`.

Look into Swagger for documentation