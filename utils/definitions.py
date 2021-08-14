class MySQL:
    host = "localhost"
    port = "3306"
    username = "ravishankar"
    password = "coderBLACK@1996"


class Schema:
    DB = "identity_management"
    Users = "users"


class RequestValidation:
    user_create_mandatory = ["name", "email_id", "password"]
    user_login_mandatory = ["email_id", "password"]


class Status:
    SUCCESS = "success"
    FAILED = "failed"
