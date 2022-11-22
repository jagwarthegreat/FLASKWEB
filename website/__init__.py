from flask import Flask
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="flask"
)

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'aksjdhaksjdhbcbcvbcvkbjlkjm'

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	return app