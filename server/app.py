#!/usr/bin/env python3
from . import app, db
from flask import Flask, jsonify, request, make_response, current_app
from .models import db, Platform, Admin, User, Publication, Communication_channel, Orders, Payment
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from datetime import datetime, timedelta
#from flask_jwt_extended import jwt_required, get_jwt_identity, JWTManager
# app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://content_management:SHAR0007@localhost/content_management_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)

# db.init_app(app)

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
                "created_at": admin.created_at
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
        if request.method == "GET":
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
                "created_at": user.created_at
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
        if request.method == "GET":
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
                "orders": platform.orders,
                "created_at":platform.created_at
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
        if request.method == "GET":
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



@app.route('/publication', methods=['GET', 'POST', 'DELETE'])
def publications():
    if request.method == 'GET':
        publications = []
        for publication in Publication.query.all():
            publication_dict = {
                "id":publication.id,
                "typeOfPublication": publication.typeOfPublication,
                "status": publication.status,
                
                
                "created_at":publication.created_at,

            }
            publications.append(publication_dict)
        response = make_response(
            jsonify(publications),
            200
        )    
        return response

    elif request.method == 'POST':
        new_publication = Publication(
            typeOfPublication = request.form.get("typeOfPublication"),
            status = request.form.get("status"),
            created_at = request.form.get("created_at"),
            

        )    
        db.session.add(new_publication)
        db.session.commit()
        publication_dict = new_publication.to_dict()

        response = make_response(
            jsonify(publication_dict),
            201
        )
        return response

@app.route('/publication/<int:id>', methods=['GET','PATCH','DELETE'])
def publications_by_id(id):
    publication =  Publication.query.filter_by(id=id).first() 
    if publication == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
        if request.method == "DELETE":
            db.session.delete(publication)
            db.session.commit()
            response_body = {
                "delete_successful": True,
                "message": " deleted."
            }
            response = make_response(
                jsonify(response_body),
                200
            )
            return response
        elif request.method == 'GET':
            publication_dict = publication.to_dict()

            response = make_response(
                jsonify(publication_dict),
                200
            )

            return response

        elif request.method == 'PATCH':
            #publication = Publication.query.filter_by(id=id).first()
            
            for attr in request.form:
                setattr(publication, attr, request.form.get(attr))

            db.session.add(publication)
            db.session.commit()

            publication_dict = publication.to_dict()
            
            response = make_response(
                jsonify(publication_dict),
                200
            )

            return response

@app.route('/communication', methods=['GET', 'POST', 'DELETE'])
def communications():
    if request.method == 'GET':
        communications = []
        for communication in Communication_channel.query.all():
            communication_dict = {
                "Message": communication.Message,
                "userId": communication.status,
                "AdminId": communication.orders,
                "created_at":communication.created_at,

            }
            communications.append(communication_dict)
        response = make_response(
            jsonify(communications),
            200
        )    
        return response

    elif request.method == 'POST':
        new_communications = Communication_channel(
            Message = request.form.get("Message"),
            userId = request.form.get("userId"),
            AdminId = request.form.get("AdminId"),
            

        )    
        db.session.add(new_communications)
        db.session.commit()
        communication_dict = new_communications.to_dict()

        response = make_response(
            jsonify(communication_dict),
            201
        )
        return response

@app.route('/communication/<int:id>', methods=['GET','PATCH','DELETE'])
def communications_by_id(id):
    communication =  Communication_channel.query.filter_by(id=id).first() 
    if communication == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
        if request.method == "DELETE":
            db.session.delete(communication)
            db.session.commit()
            response_body = {
                "delete_successful": True,
                "message": " deleted."
            }
            response = make_response(
                jsonify(response_body),
                200
            )
            return response
        elif request.method == 'GET':
            communication_dict = communication.to_dict()

            response = make_response(
                jsonify(communication_dict),
                200
            )

            return response

        elif request.method == 'PATCH':
            communication = Communication_channel.query.filter_by(id=id).first()

            for attr in request.form:
                setattr(communication, attr, request.form.get(attr))

            db.session.add(communication)
            db.session.commit()

            communication_dict = communication.to_dict()

            response = make_response(
                jsonify(communication_dict),
                200
            )

            return response 

@app.route('/orders', methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        orders = Orders.query.order_by(Orders.Type).all()
        orders_list = []
        for order in orders:
            order_dict = {
                "id": order.id,
                "Type": order.Type,
                "UnitPrice": str(order.UnitPrice),
                "status": order.status,
                "publication_id": order.publication_id,
                "user_id": order.user_id,
                "platform_id": order.platform_id,
                "platform": order.platform.to_dict() if order.platform else None, 
                "publication": order.publication.to_dict() if order.publication else None,
                "created_at": order.created_at,
            }
            orders_list.append(order_dict)

        return jsonify(orders_list)


    elif request.method == 'POST':
        new_order = Orders(
            Type = request.form.get("Type"),
            UnitPrice = request.form.get("UnitPrice"),
            status = request.form.get("status"),
            publication_id = request.form.get("publication_id"),
            platform_id = request.form.get("platform_id"),            
            user_id = request.form.get("user_id"),          
            

        )    
        db.session.add(new_order)
        db.session.commit()
        order_dict = new_order.to_dict()

        response = make_response(
            jsonify(order_dict),
            201
        )
        return response

@app.route('/orders/<int:id>', methods=['GET','PATCH','DELETE'])
def orders_by_id(id):
    order =  Orders.query.filter_by(id=id).first() 
    if order == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
        if request.method == "DELETE":
            db.session.delete(order)
            db.session.commit()
            response_body = {
                "delete_successful": True,
                "message": " deleted."
            }
            response = make_response(
                jsonify(response_body),
                200
            )
            return response
        elif request.method == 'GET':
            order_dict = order.to_dict()

            response = make_response(
                jsonify(order_dict),
                200
            )

            return response

        elif request.method == 'PATCH':
            order = Orders.query.filter_by(id=id).first()

            for attr in request.form:
                setattr(order, attr, request.form.get(attr))

            db.session.add(order)
            db.session.commit()

            order_dict = order.to_dict()

            response = make_response(
                jsonify(order_dict),
                200
            )

            return response

@app.route('/payments', methods=['GET', 'POST', 'DELETE'])
def payments():
    if request.method == 'GET':
        payments = []
        for payment in Payment.query.all():
            payment_dict = {
                "id": payment.id,
                "Amount": str(payment.Amount),
                "referenceNo": payment.referenceNo,
                "paidVia": payment.paidVia,
                "order_id": payment.order_id,
                "order": payment.order.to_dict() if payment.order else None,
                "created_at": payment.created_at,
            }
            payments.append(payment_dict)
        response = make_response(
            jsonify(payments),
            200
        )
        return response


    elif request.method == 'POST':
        new_payment = Payment(
            Amount = request.form.get("Amount"),
            referenceNo = request.form.get("referenceNo"),
            paidVia = request.form.get("paidVia"), 
            order_id = request.form.get("order_id"),      
            

        )    
        db.session.add(new_payment)
        db.session.commit()
        payment_dict = new_payment.to_dict()

        response = make_response(
            jsonify(payment_dict),
            201
        )
        return response

@app.route('/payments/<int:id>', methods=['GET','PATCH','DELETE'])
def payments_by_id(id):
    payment =  Payment.query.filter_by(id=id).first() 
    if payment == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
        if request.method == "DELETE":
            db.session.delete(payment)
            db.session.commit()
            response_body = {
                "delete_successful": True,
                "message": " deleted."
            }
            response = make_response(
                jsonify(response_body),
                200
            )
            return response
        elif request.method == 'GET':
            payment_dict = payment.to_dict()

            response = make_response(
                jsonify(payment_dict),
                200
            )

            return response

        elif request.method == 'PATCH':
            payment = Payment.query.filter_by(id=id).first()

            for attr in request.form:
                setattr(payment, attr, request.form.get(attr))

            db.session.add(payment)
            db.session.commit()

            payment_dict = payment.to_dict()

            response = make_response(
                jsonify(payment_dict),
                200
            )

            return response       
@app.route('/login', methods=['POST'])
def login():
    auth= request.json
    if not auth or not auth.get("email") or not auth.get("password"):
        return make_response({
            "message" : "Please ensure you have the right details"
        }), 401
    user=User.query.filter_by(email=auth.get("email")).first()
    if not user:
        return make_response({
            "message":"Create Account"
        }), 401
    if user and check_password_hash(user.password, auth.get("password")):
        token= jwt.decode({
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(day=1)
        },
        "secret",
        "hS256")
        return make_response({
            'token':token
        }), 201
    return make_response({
        "message":" Error in logging in User"
    }), 500

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    firstName=data['firstName']
    lastName=data['lastName']
    password=data['password']
    email=data['email']                    
    status='Active'
    password_harsh= generate_password_hash(password)
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 409
    user= User(firstName=firstName,lastName=lastName, email=email, password=password_harsh, 
               status=status)

    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201



# def generate_token(user):
#     secret_key=current_app.config['JWT_SECRET_KEY']
#     expiration= datetime.utcnow()+timedelta(days=1)
#     load={
#         "sub":user.id,
#         "user_id":user.id, 
#         "exp":expiration,
#         "firstName":user.firstName,
#         "lastName":user.lastName,
#         "email":user.email,
#         "status":user.status
#     }
#     token=jwt.encode(load, secret_key, algorithm= 'HS256')
#     return token
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



