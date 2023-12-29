import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init env.
load_dotenv()

# Init the app.
app = Flask(__name__)

# Init Database
db_url = os.getenv("DATABASE_URL")
db_connection = psycopg2.connect(db_url)

# Run Server.
if __name__ == '__main__':
	app.run(debug=True)