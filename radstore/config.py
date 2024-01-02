import os
from .dbContext import db, ma
from .models import Brand, Product, User
from .controllers.productController import productController
from .controllers.brandController import brandController

def set_up(app):

	# Init Database
	db_url = os.getenv("DATABASE_URL")
	app.config['SQLALCHEMY_DATABASE_URI'] = db_url
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Init enviroment
	db.init_app(app)
	ma.init_app(app)

	# Init and register the controllers routers
	app.register_blueprint(productController)
	app.register_blueprint(brandController)

	# Init database models
	with app.app_context():
		db.create_all()

	return app