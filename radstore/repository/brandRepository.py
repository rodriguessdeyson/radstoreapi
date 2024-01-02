from flask import jsonify
from ..dbContext import db, ma
from ..models.Brand import Brand

# Brand Schemas
class BrandSchema(ma.Schema):
	class Meta:
		fields = ('id', 'name')

brand_schema = BrandSchema()
brands_schema = BrandSchema(many = True)

def insert(brand):
	db.session.add(brand)
	db.session.commit()

	return brand_schema.jsonify(brand)

def select_all():
	products = Brand.query.all()
	result = brands_schema.dump(products)

	return jsonify(result)

def select(brandId):
	brand = Brand.query.get(brandId)

	return brand_schema.jsonify(brand)

def delete(brandId):
	brand = Brand.query.get(brandId)
	db.session.delete(brand)
	db.session.commit()