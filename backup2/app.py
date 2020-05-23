from flask import Flask,request
from flask_restful import Resource , Api ,reqparse
from flask_jwt import JWT , jwt_required
from security import authenticate,idenitiy
from Resource.user import UserRegister
from Resource.Item import Items , ItemsList

app = Flask(__name__)
app.secret_key = "mustafa"
api = Api(app)

jwt = JWT(app,authenticate,idenitiy)


api.add_resource(Items,'/Items/<string:name>')
api.add_resource(ItemsList,'/Items')
api.add_resource(UserRegister,'/Register')

if __name__ == "__main__":
    app.run(port=5000,debug=True)