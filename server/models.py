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

    @property
    def serialize(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at
        }

    def __repr__(self):
        return f'<Admin {self.firstName} {self.id}'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-orders.user','-publications.user',)
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Orders', backref="user")
    publication = db.relationship('Publication', backref="publication")
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Platform(db.Model, SerializerMixin):
    __tablename__ = 'platforms'
    serialize_rules = ('-orders.platform',)
    id = db.Column(db.Integer, primary_key = True)
    Publisher = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.String(1000), nullable=False)
    Image = db.Column(db.String(500), nullable=False)
    Amount = db.Column(db.Numeric(10,2))
    orders = db.relationship('Orders', backref="platforms")
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Publication(db.Model, SerializerMixin):
    __tablename__ = 'publications'
    serialize_rules = ('-orders.publication',)
    id = db.Column(db.Integer, primary_key = True)
    typeOfPublication = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    orders = db.relationship('Orders', backref="publication")
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Communication_channel(db.Model, SerializerMixin):
    __tablename__ = 'communication_channels'
    id = db.Column(db.Integer, primary_key = True)
    Message = db.Column(db.String(1000), nullable=False)
    userId = db.Column(db.Integer)
    AdminId = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Orders(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    serialize_rules = ('-orders',)
    id = db.Column(db.Integer, primary_key = True)
    Type = db.Column(db.String(100), nullable=False)
    UnitPrice = db.Column(db.Numeric(10,2))
    status = db.Column(db.String(200), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    platformId = db.Column(db.Integer, db.ForeignKey('platforms.id'))
    publicationId = db.Column(db.Integer, db.ForeignKey('publications.id'))
    payment = db.relationship('Payment', backref="order")
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    serialize_rules = ('-order',)
    id = db.Column(db.Integer, primary_key = True) 
    Amount = db.Column(db.Numeric(10,2))
    referenceNo = db.Column(db.Integer, nullable=False)
    paidVia = db.Column(db.String(100), nullable=False)  
    OrderId = db.Column(db.Integer, db.ForeignKey('orders.id'))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
