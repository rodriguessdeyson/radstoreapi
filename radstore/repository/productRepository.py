from flask import jsonify
from ..dbContext import db, ma
from ..models.Product import Product

# Product Schemas
class ProductSchema(ma.Schema):
	class Meta:
		fields = ('id', 'brandId', 'name', 'description','price', 'quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

def insert(product):
	db.session.add(product)
	db.session.commit()

	return product_schema.jsonify(product)

def select_all():
	products = Product.query.all()
	result = products_schema.dump(products)

	return jsonify(result)

def select(productId):
	product = Product.query.get(productId)

	return product_schema.jsonify(product)

def delete(productId):
	product = Product.query.get(productId)
	db.session.delete(product)
	db.session.commit()