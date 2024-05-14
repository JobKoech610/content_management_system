from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import stripe
import os


app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://content_management:SHAR0007@localhost/content_management_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'q|Ww8M#moj->)[SMoSw&)]m-xB0EE[^3'


stripe_keys= {
    "secret_key":os.environ["STRIPE_SECRET_KEY"],
    "publishable_key":os.environ["STRIPE_PUBLISHABLE_KEY"],
}

stripe.api_key=stripe_keys['secret_key']


migrate = Migrate(app, db)

db.init_app(app)
jwt= JWTManager(app)
