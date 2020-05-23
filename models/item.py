import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'


    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer , db.ForeignKey('store.id'))
    store = db.relationship('StoreModel')



    def __init__(self,item,price,store_id):
        self.item = item
        self.price = price
        self.store_id = store_id

    def json(self):
        print(self.price)
        print(self.item)
        return {'name':self.item , 'price':self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_item_byname(cls,item):
        return cls.query.filter_by(item = item).first()


    def delete_item(self):
        db.session.delete(self)
        db.session.commit()

