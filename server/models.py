#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class Admin(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password =db.Column(db.String)

class User(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.String)
    lastName= db.Column(db.String)
    phoneNumber= db.Column(db.Interger)
    email = db.Column(db.String)
    password =db.Column(db.String)


class Platform(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    publisher= db.Column(db.String)
    description = db.Column(db.String)
    image =db.Column(db.String)

class Orders(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    orderType = db.Column(db.String)
    date= db.Column(db.String)
    unitPrice =db.Column(db.String)
    orderStatus= db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Publication(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    publicationType= db.Column(db.String)
    publicationStatus = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Payment(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String)
    amount = db.Column(db.Integer)
    refenceNo = db.Column(db.String)
    paidVia = db.Column(db.String)

class Channel(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String)
    image = db.Column(db.String)