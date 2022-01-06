from flask import Flask, Blueprint, render_template, send_file
from flask_login import login_required, current_user

from project.models import Product
from . import db
import os

main = Blueprint('main', __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
base_image_directory = os.path.join(APP_ROOT, 'images\\base')
product_image_directory = os.path.join(APP_ROOT, 'images\\products')

#Methods


def getPriorityProducts(type: str):
    products = Product.query.filter_by(type=type, priority=True)
    return products, len([x.id for x in products])


#Endpoihts

@main.route('/')
def index():
    vintage = getPriorityProducts("Vintage")
    return render_template('index.html', vintageProducts = vintage[0], vintageSize = vintage*240)

@main.route("/image/<file>")
def image(file):
    filename = os.path.join(base_image_directory, file)
    return send_file(filename, mimetype='image/png')

@main.route("/product/<file>")
def productImage(file):
    filename = os.path.join(product_image_directory, file)
    return send_file(filename, mimetype='image/png')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)