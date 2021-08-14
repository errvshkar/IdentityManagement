import json

from flask import request
from flask_restful import Resource

from app.api.v1.Users.actions import UserActions


class Users(Resource):
    def __init__(self):
        self.actions = UserActions()

    def get(self, action_name=None):
        return dict(status="success", data="connect successfully")

    def post(self, action_name=None):
        req_body = json.loads(request.data)
        if action_name == "create":
            status = self.actions.create_user(req_body)
        if action_name == "authenticate":
            status = self.actions.authenticate_user(req_body)
        return status

    def put(self, action_name=None):
        return dict(status="success", data="connect successfully")

    def delete(self, action_name=None):
        return dict(status="success", data="connect successfully")
