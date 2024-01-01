from flask import Blueprint, request, jsonify, make_response

from ..extensions import db, ma
from ..models.Product import Product
from ..services import productService

productController = Blueprint('productController', __name__)

@productController.route('/product', methods = ['POST'])
def create_product():
	name = request.json['name']
	brandId = request.json['brandId']
	description = request.json['description']
	price = request.json['price']
	quantity = request.json['quantity']

	created_product = productService.add_product(name, brandId, description, price, quantity)
	response = make_response(created_product, 201)
	return response

@productController.route('/product', methods = ['GET'])
def get_products():
	return productService.get_all()