from flask import Blueprint, request, make_response

from ..dbContext import db, ma
from ..models.Brand import Brand
from ..services import brandService

brandController = Blueprint('brandController', __name__)

@brandController.route('/brand', methods = ['POST'])
def create_product():
	name = request.json['name']
	products = request.json['products']
	created_brand = brandService.add_brand(name, products)
	response = make_response(created_brand, 201)
	return response

@brandController.route('/brand', methods = ['GET'])
def get_products():
	brands = brandService.get_all()
	return make_response(brands, 200)

@brandController.route('/brand/<brandId>', methods = ['GET'])
def get_product(brandId):
	product = brandService.get(brandId)
	return make_response(product, 200)

@brandController.route('/brand/<brandId>', methods = ['DELETE'])
def delete_product(brandId):
	brandService.delete(brandId)
	return make_response(f'Brand {brandId} was succesfully deleted', 204)