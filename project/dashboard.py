from flask import Blueprint , render_template, redirect, url_for, request, flash, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import Product
from . import db
from .images import saveProductImage
import os
from PIL import Image

dashboard = Blueprint('dashboard', __name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
base_image_directory = os.path.join(APP_ROOT, 'images\\base')
product_image_directory = os.path.join(APP_ROOT, 'images\\products')

def getProductList():
    productList = db.session.query(Product).all()
    return productList

@dashboard.route('/dashboard')
def main():
    return render_template('dashboard.html', productList = getProductList())

@dashboard.route("/product/Thumbnail_Image_<file>")
def image(file):
    file = 'Thumbnail_Image_'+str(file)
    filename = os.path.join(product_image_directory, file)
    return send_file(filename, mimetype='image/png')

@dashboard.route('/addProduct', methods=['POST'])
def addProduct():
    productType = request.form.get('productType')
    productName = request.form.get('productName')

    # if Product.query.filter_by(productName=productName):
    #     flash('Make sure product name is unique. Product with name \''+ productName + '\' already exists')
    #     return redirect(url_for('dashboard.main'))

    try:
        productPrice = float(request.form.get('productPrice'))
    except:
        flash('Make sure product price is in $.$$ format')
        return redirect(url_for('dashboard.main'))

    try:
        productQuantity = int(request.form.get('productQuantity'))
    except:
        flash('Make sure product Quantity is a integer')
        return redirect(url_for('dashboard.main'))

    New_Product = Product(productType=productType, productName=productName, productPrice=productPrice, productQuantity=productQuantity)
    db.session.add(New_Product)
    db.session.commit()

    productID = New_Product.id
    imageFile = request.files.get('myFile')

    try:
        saveProductImage(productID, imageFile)
    except:
        flash('Make sure product image is jpg, jpeg, or png')
        return redirect(url_for('dashboard.main'))

    return redirect(url_for('dashboard.main'))
