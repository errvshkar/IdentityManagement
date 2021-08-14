import uuid
import re
import hashlib

from utils.definitions import RequestValidation
from utils.definitions import Status
from utils.definitions import Schema
from utils.models import Users
from utils.database import create_session


class UserActions(object):
    def __init__(self):
        pass

    @staticmethod
    def validate_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, email)):
            return dict(status=Status.FAILED, message="Invalid email given")

    @staticmethod
    def validate_request(validate, request):
        request_keys = request.keys()
        if validate == "user_create":
            needed_keys = list(set(RequestValidation.user_create_mandatory) - set(request_keys))
            if needed_keys:
                return dict(status=Status.FAILED, message="Mandatory details missing. "
                                                          "Required fields : {}".format(",".join(needed_keys)))
        elif validate == "user_validate":
            needed_keys = list(set(RequestValidation.user_login_mandatory) - set(request_keys))
            if needed_keys:
                return dict(status=Status.FAILED, message="Mandatory details missing. "
                                                          "Required fields : {}".format(",".join(needed_keys)))

    @staticmethod
    def password_hashing(pass_string):
        hashed_password = hashlib.sha512(pass_string.encode())
        return hashed_password.hexdigest()

    @staticmethod
    def verify_password(hashed_password, user_password):
        if hashed_password == hashlib.sha512(user_password.encode()).hexdigest():
            return True
        else:
            return False

    def authenticate_user(self, req_body):
        try:
            validate_request_failed = self.validate_request("user_validate", req_body)
            if validate_request_failed:
                return validate_request_failed
            create_user_session = create_session(Schema.DB)
            session = create_user_session()
            result = session.query(Users).filter(Users.email_id == req_body["email_id"])
            if not result.count():
                return dict(status=Status.FAILED, message="User Not Found")
            for row in result:
                if self.verify_password(row.password, req_body["password"]):
                    return dict(status=Status.SUCCESS, message="User Authenticated Successfully")
                else:
                    return dict(status=Status.FAILED, message="User Authentication Failed")
        except Exception as e:
            raise Exception(str(e))

    def create_user(self, req_body):
        try:
            validate_request_failed = self.validate_request("user_create", req_body)
            if validate_request_failed:
                return validate_request_failed
            validate_email_failed = self.validate_email(req_body["email_id"])
            if validate_email_failed:
                return validate_email_failed
            create_user_session = create_session(Schema.DB)
            user = create_user_session()
            user_detail = Users(id=str(uuid.uuid4()),
                                name=req_body["name"],
                                password=self.password_hashing(req_body["password"]),
                                email_id=req_body["email_id"])
            user.add(user_detail)
            user.commit()
            return dict(statu=Status.SUCCESS, data="User Created Successfully")
        except Exception as e:
            raise Exception(str(e))
