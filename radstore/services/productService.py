from ..models.Product import Product
from ..repository import productRepository

def add_product(name, brandId, description, price, quantity):
	new_product = Product(name, brandId, description, price, quantity)
	return productRepository.insert(new_product)

def get_all():
	return productRepository.select_all()

def get(productId):
	product = productRepository.select(productId)
	return product


def delete(productId):
	productRepository.delete(productId)