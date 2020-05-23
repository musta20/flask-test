from flask_restful import reqparse ,Resource 
from models.store import StoreModel
import sqlite3
import json

item = []

class Store(Resource):
      def get(self,name):
          store = StoreModel.get_item_byname(name)
          if store:
              return store.json()
          return {"error"},404
          
      def post(self,name):
          if StoreModel.get_item_byname(name):
             return {"message": "A store with name '{}' already exict".format(name)}
          store = StoreModel(name)
          try:
             store.save_to_db()
          except:
              return {"message":"an erorr occurred while createi the sote"},500
          return store.json(),201
    
      def delete(self,name):
          store  =  StoreModel.get_item_byname(name)
          if store:
            store.delete_item()
            return {"message":"store deleted"}
          return {"message":"item dos not excist"}

class StoreList(Resource):
    def get(self):
        return {"item":list(map(lambda x:x.json() , StoreModel.query.all()))}




