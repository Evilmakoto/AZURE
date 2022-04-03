from flaskr import db


class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    category = db.Column(db.String(32))
    type = db.Column(db.String(32))
    price = db.Column(db.Integer)

    def __init__(self, id, name, category, type, price):
        self.id = id
        self.name = name
        self.category = category
        self.type = type
        self.price = price
