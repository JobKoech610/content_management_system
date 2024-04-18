#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db =SQLAlchemy()

class Admin(db.Model, SerializerMixin):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-orders.user','-publications.user',)
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String)
    lastName = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    status = db.Column(db.String)
    orders = db.relationship('Orders', backref="user")
    publication = db.relationship('Publication', backref="publication")


class Platform(db.Model, SerializerMixin):
    __tablename__ = 'platforms'
    serialize_rules = ('-orders.platform',)
    id = db.Column(db.Integer, primary_key = True)
    Publisher = db.Column(db.String)
    Description = db.Column(db.String)
    Image = db.Column(db.String)
    Amount = db.Column(db.String)
    orders = db.relationship('Platforms', backref="user")
    

class Publication(db.Model, SerializerMixin):
    __tablename__ = 'publications'
    serialize_rules = ('-orders.publication')
    id = db.Column(db.Integer, primary_key = True)
    typeOfPublication = db.Column(db.String)
    status = db.Column(db.String)
    orders = db.relationship('Orders', backref="publication")
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))


class Communication_channel(db.Model, SerializerMixin):
    __tablename__ = 'communication_channels'
    id = db.Column(db.Integer, primary_key = True)
    Message = db.Column(db.String)
    userId = db.Column(db.Integer)
    AdminId = db.Column(db.Integer)

class Orders(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    serialize_rules = ('-payments.order',)
    id = db.Column(db.Integer, primary_key = True)
    Type = db.Column(db.String)
    UnitPrice = db.Column(db.String)
    status = db.Column(db.String)
    Date = db.Column(db.String)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    platformId = db.Column(db.Integer, db.ForeignKey('platforms.id'))
    publicationId = db.Column(db.Integer, db.ForeignKey('publications.id'))
    orders = db.relationship('Payment', backref="order")

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key = True) 
    Amount = db.Column(db.Integer)
    referenceNo = db.Column(db.Integer)
    paidVia = db.Column(db.String)  
    Date = db.Column(db.String)
    OrderId = db.Column(db.Integer, db.ForeignKey('orders.id'))

