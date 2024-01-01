from ..extensions import db

class User(db.Model):
	__tablename__ = 'user'
	__table_args__ = {'schema': 'radstore'}
	id = db.Column(db.Integer, primary_key=True)
	firstName = db.Column(db.String(100))
	secondName = db.Column(db.String(100))
	email = db.Column(db.String(100))
	username = db.Column(db.String(100))

	def __init__(self, firstName, secondName, email, username):
		self.firstName = firstName
		self.secondName = secondName
		self.email = email
		self.username = username