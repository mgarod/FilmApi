from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    pass

class UnauthorizedError(HTTPException):
    pass

class EmailAlreadyExistsError(HTTPException):
    pass

class UsernameAlreadyExistsError(HTTPException):
    pass

class InvalidPageError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UsernameAlreadyExistsError": {
        "message": "User with given username already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "InvalidPageError": {
        "message": "Invalid page selection",
        "status": 422
    },
}