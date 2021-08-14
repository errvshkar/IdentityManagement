from flask import Flask
from flask_restful import Api

from app.api.v1.Users.route import Users

app = Flask("IdentityManagement")

api = Api(app)

api.add_resource(Users,
                 '/v1/art/user/<action_name>'
                 )
