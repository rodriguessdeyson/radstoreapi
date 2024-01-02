from flask import Blueprint, request, make_response

from ..dbContext import db, ma
from ..models.Product import Product
from ..services import productService

productController = Blueprint('productController', __name__)

@productController.route('/product', methods = ['POST'])
def create_product():
	name        = request.json['name']
	brandId     = request.json['brandId']
	description = request.json['description']
	price       = request.json['price']
	quantity    = request.json['quantity']

	created_product = productService.add_product(name, brandId, description, price, quantity)
	response = make_response(created_product, 201)
	return response

@productController.route('/product', methods = ['GET'])
def get_products():
	products = productService.get_all()
	return make_response(products, 200)

@productController.route('/product/<productId>', methods = ['GET'])
def get_product(productId):
	product = productService.get(productId)
	if product:
		return make_response(product, 200)
	else:
		return make_response(204)

@productController.route('/product/<productId>', methods = ['DELETE'])
def delete_product(productId):
	productService.delete(productId)
	return make_response(f'Product {productId} was succesfully deleted', 204)