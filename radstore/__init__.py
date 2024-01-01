import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import db
from .models.Product import *
from .config import set_up

# Init env.
load_dotenv()

def create_app():
	app = Flask(__name__)
	
	# Init enviroment, database.
	set_up(app)

	return app