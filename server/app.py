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
    

@app.route('/admin/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def admin_by_id(id):
    admin = Admin.query.filter_by(id=id).first()
    if admin == None:
        response_body ={
            "message": "This admin doesn't exist"
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else: 
        if response.method == "GET":
            admin_dict = admin.to_dict()
            response = make_response(
                jsonify(admin.to_dict()), 200
            )
            return response
        elif request.method == 'PATCH':
            admin = Admin.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(admin, attr, request.form.get(attr))
            
            db.session.add(admin)
            db.session.commit()

            admin_dict = admin.to_dict()
            response = make_response(
                jsonify(admin_dict)
            )
            return response
        elif request.method == 'DELETE':
            db.session.delete(admin)
            db.session.commit()
            response_body ={
                "delete_successful" :True,
                "message" : "Admin Deleted"
            }
            response = make_response(
                jsonify(response_body), 200
            )
            return response
        else:
            # Handle unsupported methods
            response_body = {
                "message": "Method not allowed for this endpoint."
            }
            response = make_response(jsonify(response_body), 405)
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


@app.route('/user/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def users_by_id(id):
    user = User.query.filter_by(id=id).first()
    if user == None:
        response_body ={
            "message": "This user doesn't exist"
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else: 
        if response.method == "GET":
            user_dict = user.to_dict()
            response = make_response(
                jsonify(user.to_dict()), 200
            )
            return response
        elif request.method == 'PATCH':
            user = User.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(user, attr, request.form.get(attr))
            
            db.session.add(user)
            db.session.commit()

            user_dict = user.to_dict()
            response = make_response(
                jsonify(user_dict)
            )
            return response
        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()
            response_body ={
                "delete_successful" :True,
                "message" : "User Deleted"
            }
            response = make_response(
                jsonify(response_body), 200
            )
            return response
        else:
            # Handle unsupported methods
            response_body = {
                "message": "Method not allowed for this endpoint."
            }
            response = make_response(jsonify(response_body), 405)
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
@app.route('/platforms/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def platform_by_id(id):
    platform = Platform.query.filter_by(id=id).first()
    if platform == None:
        response_body ={
            "message": "This user doesn't exist"
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else: 
        if response.method == "GET":
            platform_dict = platform.to_dict()
            response = make_response(
                jsonify(platform.to_dict()), 200
            )
            return response
        elif request.method == 'PATCH':
            platform = Platform.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(platform, attr, request.form.get(attr))
            
            db.session.add(platform)
            db.session.commit()

            platform_dict = platform.to_dict()
            response = make_response(
                jsonify(platform_dict)
            )
            return response
        elif request.method == 'DELETE':
            db.session.delete(platform)
            db.session.commit()
            response_body ={
                "delete_successful" :True,
                "message" : "User Deleted"
            }
            response = make_response(
                jsonify(response_body), 200
            )
            return response
        else:
            # Handle unsupported methods
            response_body = {
                "message": "Method not allowed for this endpoint."
            }
            response = make_response(jsonify(response_body), 405)
            return response
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)