#!/usr/bin/env python3
from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Admin {self.firstName} {self.id}'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-orders.user',)
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    orders = db.relationship('Orders', backref='user')

    
    def __repr__(self):
        return f'<User {self.firstName} {self.id}'      


class Platform(db.Model, SerializerMixin):
    __tablename__ = 'platforms'
    serialize_rules = ('-orders.platform',)
    id = db.Column(db.Integer, primary_key = True)
    Publisher = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(1000), nullable=False)
    Image = db.Column(db.String(500), nullable=False)
    Amount = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    orders = db.relationship('Orders', backref='platform')
   
    def __repr__(self):
        return f'<Platform {self.Publisher} {self.id}>'

class Publication(db.Model, SerializerMixin):
    __tablename__ = 'publications'
    serialize_rules = ('-orders.publication',)
    id = db.Column(db.Integer, primary_key = True)
    typeOfPublication = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    orders = db.relationship('Orders', backref='publication')

    def __repr__(self):
        return f'<Publication {self.typeOfPublication} {self.id}'


class Orders(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    serialize_rules = ('-publication.orders', '-user.orders', '-platform.orders', '-payment.order',)
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(100), nullable=False)
    UnitPrice = db.Column(db.Numeric(10, 2))
    status = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    publication_id = db.Column(db.Integer, db.ForeignKey('publications.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platforms.id'))
    payment = db.relationship('Payment', uselist = False, backref='order') #one-to-one relationship
    def __repr__(self):
        return f'<Type {self.Type} {self.id}>'


  


class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    serialize_rules = ('-order.payment',)
    id = db.Column(db.Integer, primary_key=True)
    Amount = db.Column(db.Numeric(10, 2))
    referenceNo = db.Column(db.Integer, nullable=False)
    paidVia = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    def __repr__(self):
        return f'<Amount {self.Amount} {self.id}'

class Communication_channel(db.Model, SerializerMixin):
    __tablename__ = 'communication_channels'
    id = db.Column(db.Integer, primary_key = True)
    Message = db.Column(db.String(1000), nullable=False)
    userId = db.Column(db.Integer)
    AdminId = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Communication_channel {self.Message} {self.id}'