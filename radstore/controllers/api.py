from flask import Blueprint

from ..extensions import db, ma
from ..models.Brand import Brand

api = Blueprint('api', __name__)

@api.route('/brand/<name>')
def create_product(name):
	brand = Brand.query.filter_by(name='nestlé').first()

	return {'brand': brand.name}