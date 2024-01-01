import os
from .extensions import db, ma
from .models import Brand, Product, User
from .controllers.productController import productController
from .controllers.api import api

def set_up(app):

	# Init Database
	db_url = os.getenv("DATABASE_URL")
	app.config['SQLALCHEMY_DATABASE_URI'] = db_url
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	# Init enviroment
	db.init_app(app)
	ma.init_app(app)

	# Init the controllers/router
	app.register_blueprint(productController)
	app.register_blueprint(api)

	# Init database models
	with app.app_context():
		db.create_all()

	return app