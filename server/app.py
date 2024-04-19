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

@app.route('/admin', methods=['GET'])
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
@app.route('/user', methods=['GET'])
def users():
    if request.method == 'GET':
        users=[]
        for user in User.query.all():
            user_dict ={
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "status": user.status,
                "orders": user.orders,
                "publication":user.publication
            }
            users.append(user_dict)
        response = make_response(
            jsonify(users), 200
        )
        return response

@app.route('/platforms', methods=['GET'])
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



# @app.route('/companies', methods=['GET', 'POST', 'DELETE'])
# def companies():
#     if request.method == 'GET':
#         companies = []
#         for company in Company.query.all():
#             # company_dict = company.to_dict()
#             company_dict = {
#                 "company_name": company.company_name,
#                 "class_type": company.class_type,
#                 "location": company.location,
#                 "size": company.size,
#                 "account": company.account,

#             }
#             companies.append(company_dict)
#         response = make_response(
#             jsonify(companies),
#             200
#         )    
#         return response
#     elif request.method == 'POST':
#         new_company = Company(
#             company_name = request.form.get("company_name"),
#             class_type = request.form.get("class_type"),
#             location = request.form.get("location"),
#             size = request.form.get("size"),
#             account = request.form.get("account"),
#         )    
#         db.session.add(new_company)
#         db.session.commit()
#         review_dict = new_company.to_dict()

#         response = make_response(
#             jsonify(review_dict),
#             201
#         )
#         return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)