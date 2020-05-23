from flask import Flask,request
from flask_restful import Resource , Api ,reqparse
from flask_jwt import JWT , jwt_required
from security import authenticate,idenitiy
app = Flask(__name__)
app.secret_key = "mustafa"
api = Api(app)

jwt = JWT(app,authenticate,idenitiy)
items = []
class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required = True,help='this field cant be empty')

    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name']==name , items),None)
        return {'item':item}, 200 if item is not None else 404

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name']!=name , items))
        return {"message":'item deleted'}

    def post(self,name):
        if next(filter(lambda x:x['name']==name , items),None) is not None:
            return {"messafe":"an item with '{}' found".format(name)}, 400
        data = Items.parser.parse_args()

        item = {'name':name,'price':data['price']}
        items.append(item)
        return item, 201
    
    def put(self,name):

        data = Items.parser.parse_args()
        item = next(filter(lambda x: x['name']==name , items),None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemsList(Resource):
    def get(self):
        return items



api.add_resource(Items,'/Items/<string:name>')
api.add_resource(ItemsList,'/Items')


app.run(port=5000,debug=True)