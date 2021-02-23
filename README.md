# Film Database API
This is a Toy API I was building in my own time. The goal of this Toy API was to create a project beyond simply using raw Flask alone. I was inspired by a [guide](https://dev.to/paurakhsharma/series/3672) but took some liberties with it like using SQL instead of MongoDB.

I was able utilize the `Flask-RESTful` package, `Flask-SQLAlchemy` and SQlite for the ORM, add user sign up and login with `Flask-bcrypt` and `Flask-JWT-Extended`, and add some unit tests using the standard library `unittest`.

Functions surrounding the Film portion of the database is more or less fully realized. The portions regarding sign up and login are functional although enforcement is mostly disabled. The enforcment was commented out (`@jwt_required`) because I did not want to have to log in while running the unit tests. This is something I would address in the future.

### Database Initialization
Prior to running the API, please run `python init_db.py` to create and enter dummy data into the database

### Tests
```
ENV_FILE_LOCATION=tests/.env.test python3 -m unittest
```

There are some issues regarding relative imports. As such, tests are required to be run from the root of the project, and point 

Database calls are not mocked. The test class will set up a (smaller) real DB called `test.db`, though in this case, nearly identical to the production db since there are only a few data points.

Database initialization happens in `setUp` which likely should be done with `setUpClass` to only run `init_db()` once per class, not every `test_*` method.

Test coverage is incomplete. There are currently no tests for anything related to Users, login, authentication nor authorization.


### Other Issues
The .env files would not be included in this or any project as they contain secrets and exclusion would be enforced by the `.gitignore` file. For the purpose of simplicity they are added here and removed from the `.gitignore` file.

There is very little manual handling for bad calls, bad data, incomplete calls, etc. Since I intended this to be a toy project, this was not my focus. However, the libraries used in this project do cover a fair deal. For example, `RequestParser` has some type enforcement for request data, and I did utilize `first_or_404` with `SQLAlchemy`.