from . import db
from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey('user.id'))
    street1 = db.Column(db.String(1000))
    street2 = db.Column(db.String(1000))
    country = db.Column(db.String(100))
    state = db.Column(db.String(100))
    zipcode = db.Column(db.String(10))

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, ForeignKey('user.id'))
    phoneNumber = db.Column(db.String(1000))
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productType = db.Column(db.String(100))
    productName = db.Column(db.String(100))
    productPrice = db.Column(db.Float)
    productQuantity = db.Column(db.Integer)
