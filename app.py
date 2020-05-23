from flask import Flask,request
from flask_restful import Resource , Api ,reqparse
from flask_jwt import JWT , jwt_required
from security import authenticate,idenitiy
from Resource.user import UserRegister
from Resource.Item import Items , ItemsList
from Resource.store import Store , StoreList
from db import db
app = Flask(__name__)
app.secret_key = "mustafa"
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
jwt = JWT(app,authenticate,idenitiy)


api.add_resource(Items,'/Items/<string:name>')
api.add_resource(ItemsList,'/Items')
api.add_resource(UserRegister,'/Register')

api.add_resource(Store,'/Store/<string:name>')
api.add_resource(StoreList,'/Items')
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000,debug=True)