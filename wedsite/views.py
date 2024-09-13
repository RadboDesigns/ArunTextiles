from flask import Blueprint, render_template, flash, redirect, request, jsonify
from .models import Product,BestOffers,Instagram, BestSeller, ProductPage, Cart
from flask_login import login_required, current_user
from .forms import AdminLoginForm
from . import db

views = Blueprint('views', __name__)

API_PUBLISHABLE_KEY = 'YOUR_PUBLISHABLE_KEY'

API_TOKEN = 'YOUR_API_TOKEN'


# @views.route('/add_product_bestSeller/<int:product_id>', methods=['POST'])
# @login_required
# def add_product_bestSeller(product_id):
#     data = request.get_json()
#     quantity = data.get('quantity', 1)
#     product = BestSeller.query.get_or_404(product_id)

#     # Determine the product type
#     product_link_type = product.product_type

#     cart_item = Cart.query.filter_by(user_link=current_user.id, product_link_id=product_id).first()

#     if cart_item:
#         cart_item.quantity += quantity
#         current_quantity = cart_item.quantity
#     else:
#         new_cart_item = Cart(
#             user_link=current_user.id,
#             product_link_id=product_id,
#             product_link_type=product_link_type,
#             quantity=quantity
#         )
#         db.session.add(new_cart_item)
#         current_quantity = new_cart_item.quantity

#     db.session.commit()
    
#     return jsonify({'status': 'success', 'message': 'Product added to cart successfully!', 'quantity': current_quantity})

# @views.route('/add_product_newArrival/<int:product_id>', methods=['POST'])
# @login_required
# def add_product_newArrival(product_id):
#     data = request.get_json()
#     quantity = data.get('quantity', 1)
#     product = Product.query.get_or_404(product_id)

#     # Determine the product type
#     product_link_type = product.product_type

#     cart_item = Cart.query.filter_by(user_link=current_user.id, product_link_id=product_id).first()

#     if cart_item:
#         cart_item.quantity += quantity
#         current_quantity = cart_item.quantity
#     else:
#         new_cart_item = Cart(
#             user_link=current_user.id,
#             product_link_id=product_id,
#             product_link_type=product_link_type,
#             quantity=quantity
#         )
#         db.session.add(new_cart_item)
#         current_quantity = new_cart_item.quantity
#     print("Product added to cart successfully!")
#     db.session.commit()
#     print(current_quantity)
    
#     return jsonify({'status': 'success', 'message': 'Product added to cart successfully!', 'quantity': current_quantity})



@views.route('/')
def index():
    if current_user.is_authenticated:
        cart_items = Cart.query.filter_by(user_link=current_user.id).all()
        cart_count = len(cart_items)
    else:
        cart_count = 0
    items = Product.query.all()
    items_bestSeller = BestSeller.query.all()
    items_bestOffer = BestOffers.query.all()
    items_insta = Instagram.query.all()
    items_product = ProductPage.query.all()
    return render_template("index.html", 
                           items=items, 
                           items_bestSeller=items_bestSeller, 
                           items_bestOffer=items_bestOffer, 
                           items_insta=items_insta, 
                           items_product=items_product,
                           cart_count=cart_count)

@views.route("/about")
def about():
    if current_user.is_authenticated:
        cart_items = Cart.query.filter_by(user_link=current_user.id).all()
        cart_count = len(cart_items)
    else:
        cart_count = 0
    return render_template("about.html", cart_count=cart_count)

@views.route("/productPage", methods=['GET'])
def productPageList():
    items = ProductPage.query.all()
    if current_user.is_authenticated:
        cart_items = Cart.query.filter_by(user_link=current_user.id).all()
        cart_count = len(cart_items)
    else:
        cart_count = 0
    return render_template("productPage.html", items=items, cart_count=cart_count)

@views.route("/contact")
def contact():
    if current_user.is_authenticated:
        cart_items = Cart.query.filter_by(user_link=current_user.id).all()
        cart_count = len(cart_items)
    else:
        cart_count = 0
    return render_template("contact.html", cart_count=cart_count)

@views.route("/adminLoginPage")
def adminLoginPage():
    form = AdminLoginForm()
    return render_template("adminLoginPage.html", form=form)

