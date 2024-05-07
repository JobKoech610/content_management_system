from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://content_management:postgres@localhost:5432/content_management_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '{~T<B#c&Y@oP}"C}pc7ajYR},Etow+Sc'

migrate = Migrate(app, db)

db.init_app(app)
jwt= JWTManager(app)