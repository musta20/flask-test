import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'store'

    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic')


    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name , 'items':[item.json() for item in self.items.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_item_byname(cls,name):
        return cls.query.filter_by(name = name).first()


    def delete_item(self):
        db.session.delete(self)
        db.session.commit()

