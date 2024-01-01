from flask import Blueprint

from ..extensions import db, ma
from ..models.Brand import Brand

main = Blueprint('main', __name__)

@main.route('/brand/<name>')
def create_product(name):
	brand = Brand(name)
	db.session.add(brand)
	db.session.commit()

	return "created product!"