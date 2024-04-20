#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Platform, Admin, User

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

@app.route('/admin', methods=['GET', 'POST'])
def admins():
    if request.method == 'GET':
        admins=[]
        for admin in Admin.query.all():
            admin_dict ={
                "firstName": admin.firstName,
                "lastName": admin.lastName,
                "email": admin.email,
                "password": admin.password,
                "orders": admin.orders
            }
            admins.append(admin_dict)
        response = make_response(
            jsonify(admins), 200
        )
        return response
    elif request.method =='POST':
        new_admin= Admin(
            firstName = request.form.get('firstName'),
            lastName= request.form.get('lastName'),
            email= request.form.get('email'),
            password=request.form.get('password')
        )
        db.session.add(new_admin)
        db.session.commit()
        admins_dict=new_admin.to_dict()
        response= make_response(
            jsonify(admins_dict), 201
        )
        return response
@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users=[]
        for user in User.query.all():
            user_dict ={
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "password": user.password,
                "status": user.status,
                "orders": user.orders,
                "publication":user.publication
            }
            users.append(user_dict)
        response = make_response(
            jsonify(users), 200
        )
        return response
    elif request.method =='POST':
        new_user= User(
            firstName = request.form.get('firstName'),
            lastName= request.form.get('lastName'),
            email= request.form.get('email'),
            password=request.form.get('password'),
            status=request.form.get('status')
        )
        db.session.add(new_user)
        db.session.commit()
        users_dict=new_user.to_dict()
        response= make_response(
            jsonify(users_dict), 201
        )
        return response

@app.route('/platforms', methods=['GET', 'POST'])
def platforms():
    if request.method == 'GET':
        platforms=[]
        for platform in Platform.query.all():
            platform_dict ={
                "Publisher": platform.Publisher,
                "Description": platform.Description,
                "Image": platform.Image,
                "Amount": platform.Amount,
                "orders": platform.orders
            }
            platforms.append(platform_dict)
        response = make_response(
            jsonify(platforms), 200
        )
        return response
    elif request.method =='POST':
        new_platform= Platform(
            Publisher = request.form.get('Publisher'),
            Description= request.form.get('Description'),
            Image= request.form.get('Image'),
            Amount=request.form.get('Amount')
        )
        db.session.add(new_platform)
        db.session.commit()
        platforms_dict=new_platform.to_dict()
        response= make_response(
            jsonify(platforms_dict), 201
        )
        return response
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)