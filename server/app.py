#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from flask import db, Platform

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# api = Api(app)

@app.route('/')
def index():
    return "content management system"

@app.route('/platforms', methods=['GET'])
def platforms():
    if request.method == 'GET':
        platforms=[]
        for all platform in Platform.query.all():
            platform_dict ={
                "publisher": platform.publisher,
                "description": platform.description,
                "image": platform.image
            }
        platforms.append(platform_dict)
        response = make_response(
            jsonify(platforms), 200
        )
        return response