from flask_restful import Resource, reqparse
from db import db

class DBinit(Resource):
    def get(self):
        db.create_all()
        return {"message": "creating db."}, 201

