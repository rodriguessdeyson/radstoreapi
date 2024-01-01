from ..models.Product import Product
from ..dbContext import productRepository

def add_product(name, brandId, description, price, quantity):
	new_product = Product(name, brandId, description, price, quantity)
	return productRepository.insert(new_product)

def get_all():
	return productRepository.select_all()