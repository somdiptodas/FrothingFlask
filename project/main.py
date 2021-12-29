from flask import Flask, Blueprint, render_template, send_file
from flask_login import login_required, current_user
from . import db
import os

main = Blueprint('main', __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
base_image_directory = os.path.join(APP_ROOT, 'images\\base')
product_image_directory = os.path.join(APP_ROOT, 'images\\products')

@main.route('/')
def index():

    return render_template('index.html')

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