#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://content_management:SHAR0007@localhost/content_management_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# api = Api(app)

@app.route('/')
def index():
    return "content"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)