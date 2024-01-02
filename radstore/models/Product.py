from ..dbContext import db

class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'radstore'}
    id = db.Column(db.Integer, primary_key=True)
    brandId = db.Column(db.Integer, db.ForeignKey('radstore.brand.id'), nullable  = False)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, brandId, description, price, quantity):
        self.name = name
        self.brandId = brandId
        self.description = description
        self.price = price
        self.quantity = quantity
