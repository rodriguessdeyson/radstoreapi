from ..models.Brand import Brand
from ..repository import brandRepository

def add_brand(name, products = []):
	new_brand = Brand(name, products)
	return brandRepository.insert(new_brand)

def get_all():
	return brandRepository.select_all()

def get(brandId):
	brand = brandRepository.select(brandId)
	return brand


def delete(brandId):
	brandRepository.delete(brandId)