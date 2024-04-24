from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://content_management:SHAR0007@localhost/content_management_db'

db.init_app(app)