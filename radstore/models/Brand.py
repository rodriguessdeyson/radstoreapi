from ..extensions import db

class Brand(db.Model):
	__tablename__ = 'brand'
	__table_args__ = {'schema': 'radstore'}
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	products = db.relationship("Product", backref = "radstore.brand", lazy = True)

	def __init__(self, name):
		self.name = name