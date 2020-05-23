from flask_restful import reqparse ,Resource 
from flask_jwt import  jwt_required
from models.item import ItemModel
import sqlite3
import json

item = []

class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',type=float,required = True,
        help='this field cant be empty')
    parser.add_argument(
        'item',type= str ,required = False,
        help='this field cant be empty')
    parser.add_argument(
        'store_id',type= int ,required = True,
        help='this field cant be empty')

    @jwt_required()
    def get(self,name):
        item  = ItemModel.get_item_byname(name)
        if item:
            return item.json()
        else:
            return {"message":"Item not found"},404

    def delete(self,name):
        item = ItemModel.get_item_byname(name)
        if item is None:
            return {"messafe":"the item dost exict"}, 400
        print(item.item,item.price)
        item.delete_item()
        return {"message":'item deleted'}

    def post(self,name):
        item = ItemModel.get_item_byname(name)
        if item is not None:
            return {"messafe":"an item with '{}' found".format(name)}, 400
        else :
            data = Items.parser.parse_args()

            itemin = ItemModel(**data)
     
            itemin.save_to_db()

            return itemin.json(), 201
    
    def put(self,name):
        data = Items.parser.parse_args()
        item = ItemModel.get_item_byname(name)
        if item is None:
            item = ItemModel(name,**data)
        else:
            item.price=data['price']

        item.save_to_db()
        return item.json()
    
 

class ItemsList(Resource):
    def get(self):
        return {"item":list(map(lambda x:x.json() , ItemModel.query.all()))}
