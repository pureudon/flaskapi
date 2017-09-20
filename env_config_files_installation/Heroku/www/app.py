import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.user import UserList
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.dbinit import DBinit

from flask import render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://user:littleredflower@localhost:5432/user')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'EiEiO'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


# @app.before_first_request
# def create_tables():
#     db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


api.add_resource(DBinit, '/createdb')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
