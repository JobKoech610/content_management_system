from . import app, db

from flask import request, make_response, jsonify
from .models import Platform, Publication, Communication_channel, Orders, Payment
from werkzeug.security import generate_password_hash,check_password_hash


@app.route('/')
def index():
    return "content"

@app.route('/platform', methods=['GET', 'POST', 'DELETE'])
def platforms():
    if request.method == 'GET':
        platforms = []
        for platform in Platform.query.all():
            platform_dict = {
                "id":platform.id,
                "Publisher": platform.Publisher,
                "Description": platform.Description,
                "Image": platform.Image,
                "Amount": platform.Amount,
                "orders": platform.orders,
                "created_at":platform.created_at,

            }
            platforms.append(platform_dict)
        response = make_response(
            jsonify(platforms),
            200
        )    
        return response

    elif request.method == 'POST':
        new_platform = Platform(
            Publisher = request.form.get("Publisher"),
            Description = request.form.get("Description"),
            Image = request.form.get("Image"),
            Amount = request.form.get("Amount"),

        )    
        db.session.add(new_platform)
        db.session.commit()
        review_dict = new_platform.to_dict()

        response = make_response(
            jsonify(review_dict),
            201
        )
        return response

@app.route('/platform/<int:id>', methods=['GET','PATCH','DELETE'])
def platforms_by_id(id):
    platform =  Platform.query.filter_by(id=id).first() 
    if platform == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
        if request.method == "DELETE":
            db.session.delete(platform)
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
            platform_dict = platform.to_dict()

            response = make_response(
                jsonify(platform_dict),
                200
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
                jsonify(platform_dict),
                200
            )

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
                "orders": publication.orders,
                "userId": publication.userId,
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
        orders = Orders.query.all()
        orders_list = []
        for order in orders:
            order_dict = {
                "id": order.id,
                "Type": order.Type,
                "UnitPrice": str(order.UnitPrice),
                "status": order.status,
                "userId": order.userId,
                "platformId": order.platformId,
                "publicationId": order.publicationId,
                "created_at": order.created_at,
                "payment": []
            }
            for payment in order.payment:
                payment_dict = {
                    "id": payment.id,
                    "Amount": str(payment.Amount),
                    "referenceNo": payment.referenceNo,
                    "paidVia": payment.paidVia,
                    "created_at": payment.created_at
                }
                order_dict["payment"].append(payment_dict)
            orders_list.append(order_dict)

        return jsonify(orders_list)


    elif request.method == 'POST':
        new_order = Orders(
            Type = request.form.get("Type"),
            UnitPrice = request.form.get("UnitPrice"),
            status = request.form.get("status"),
            platformId = request.form.get("platformId"),
            publicationId = request.form.get("publicationId"),
            userId = request.form.get("userId"),

            
            

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
                "OrderId": payment.OrderId,
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
            OrderId = request.form.get("OrderId"),      
            

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





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  