from flask import Blueprint, render_template, session, redirect, request, url_for, flash, jsonify
from .models import Admin, User, ProductPage, Cart, Product, BestSeller, Order
from flask_login import login_user, login_required, logout_user, current_user
from .forms import UserSigupForm, UserLoginForm, UserProfileUpdateForm, AdminLoginForm, DummyForm, CartForm, PaymentForm
from instamojo_wrapper import Instamojo
from werkzeug.security import generate_password_hash
from .import db

API_KEY = "82bd6a328312fb45c4c16563dadbf5ed"
AUTH_TOKEN = "a15827756da4c7cec318b337e63cfd98"


auth = Blueprint('auth', __name__, url_prefix='/aruntextiles')
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)



@auth.route('/track_our_order', methods=['GET'])
@login_required
def track_our_order():
    return render_template('trackOrder.html')




@auth.route('/payment', methods=['POST'])
def pay():
    form = PaymentForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        amount = form.amount.data
        purpose = form.purpose.data
        
        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            buyer_name=name,
            send_email=True,
            send_sms=True,
            email=email,
            phone=phone,
            allow_repeated_payments=False
        )
        
        # Redirect the user to the payment URL
        return redirect(response['payment_request']['longurl'])
    return redirect(url_for('auth.cart'))

@auth.route('/remove_from_cart/<int:cart_item_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_item_id):
    form = CartForm()
    if form.validate_on_submit():
        cart_item = Cart.query.get(cart_item_id)
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
        else:
            flash('Item not found', 'error')
    else:
        flash('Form validation failed', 'error')
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'error')
    return redirect(url_for('auth.cart'))


@auth.route('/check_login_status', methods=['GET'])
def check_login_status():
    is_logged_in = current_user.is_authenticated
    return jsonify({'is_logged_in': is_logged_in})


def add_to_cart_generic(product_id, product_type):
    data = request.get_json()
    quantity = data.get('quantity', 1)

    if product_type == 'ProductPage':
        product = ProductPage.query.get_or_404(product_id)
    elif product_type == 'Product':
        product = Product.query.get_or_404(product_id)
    elif product_type == 'BestSeller':
        product = BestSeller.query.get_or_404(product_id)
    else:
        return jsonify({'status': 'error', 'message': 'Invalid product type'}), 400

    cart_item = Cart.query.filter_by(
        user_link=current_user.id,
        product_link_id=product_id,
        product_link_type=product_type
    ).first()

    if cart_item:
        cart_item.quantity += quantity
        current_quantity = cart_item.quantity
    else:
        new_cart_item = Cart(
            user_link=current_user.id,
            product_link_id=product_id,
            product_link_type=product_type,
            quantity=quantity
        )
        db.session.add(new_cart_item)
        current_quantity = new_cart_item.quantity

    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Product added to cart successfully!', 'quantity': current_quantity})


@auth.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    return add_to_cart_generic(product_id, 'ProductPage')


@auth.route('/add_product_newArrival/<int:product_id>', methods=['POST'])
@login_required
def add_product_newArrival(product_id):
    return add_to_cart_generic(product_id, 'Product')


@auth.route('/add_product_bestSeller/<int:product_id>', methods=['POST'])
@login_required
def add_product_bestSeller(product_id):
    return add_to_cart_generic(product_id, 'BestSeller')
@auth.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_link=current_user.id).all()
    
    cart_details = []
    total_amount = 0

    # Debugging: Log the cart items
    print(f"Cart items for user {current_user.id}: {cart_items}")
    
    for item in cart_items:
        product = None
        
        # Debugging: Log the product_link_type and product_link_id
        print(f"Processing cart item {item.id} with type {item.product_link_type} and ID {item.product_link_id}")

        if item.product_link_type == 'ProductPage':
            product = ProductPage.query.get(item.product_link_id)
        elif item.product_link_type == 'Product':
            product = Product.query.get(item.product_link_id)
        elif item.product_link_type == 'BestSeller':
            product = BestSeller.query.get(item.product_link_id)
        
        if product:
            cart_details.append({
                'cart_item': item,
                'product': product
            })
            total_amount += product.no_of_products_price * item.quantity
        else:
            # Debugging: Log if the product is not found
            print(f"Product not found for cart item {item.id} with type {item.product_link_type} and ID {item.product_link_id}")

    form = CartForm()
    
    # Debugging: Log the cart details
    print(f"Cart details: {cart_details}")
    
    cart_count = len(cart_items)  # Calculate the number of items in the cart
    
    return render_template('cart.html', cart_details=cart_details, total_amount=total_amount, form=form, cart_count=cart_count)


@auth.route("/userSignUp", methods=["GET", "POST"])
def userSignUp():
    form = UserSigupForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.user_name.data
        password_1 = form.password_1.data
        password_2 = form.password_2.data

        print(f"Received form data: email={email}, username={username}, password1={password_1}, password2={password_2}")

        if password_1 == password_2:
            new_customer = User(
                email=email,
                username=username,
                password_hash=generate_password_hash(password_2)
            )


            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('Account Created Successfully, You can now Login')
                print('Account Created Successfully, You can now Login')
                return redirect(url_for('auth.userSignUp'))
            except Exception as e:
                print(f"Exception occurred: {e}")
                flash('Account not Created, Email already exists')
                print('Account not Created, Email already exists')

        else:
            flash('Passwords do not match')
            print('Passwords do not match')

    print("Form validation failed or method is GET")
    return render_template("userSignupForm.html", form=form)



@auth.route("/userLogin", methods=["GET", "POST"])
def userLogin():
    form = UserLoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('User Login Successful:'+ user.username)
            return redirect(url_for('auth.userProfile', user_id=user.id))

        else:
            flash('Invalid credentials')
            return render_template('userLogin.html', form=form, error='Invalid credentials')
    return render_template("userLogin.html", form=form)

@auth.route("/userProfile/<int:user_id>")
def userProfile(user_id):
    customer = User.query.get(user_id)
    return render_template("userProfile.html", customer=customer)

@auth.route("/UserProfileUpdate", methods=["GET", "POST"])
def UserProfileUpdate():
    form = UserProfileUpdateForm()
    if form.validate_on_submit():
        customer = User.query.get(current_user.id)
        customer.firstname = form.firstname.data
        customer.email = form.email.data
        customer.phone = form.phone.data
        customer.address = form.address.data

        db.session.commit()
        return redirect(url_for('auth.UserProfileUpdate'))
    
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.email.data = current_user.email
        form.phone.data = current_user.phone
        form.address.data = current_user.address

    return render_template('customer_profile_update.html', form=form)


@auth.route("/adminLogin", methods=["GET", "POST"])
def adminLogin():
    items = Order.query.order_by(Order.id).all()
    form = AdminLoginForm()
    print("Form created:", form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Admin.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            # return redirect(url_for('auth.dashboard'))
            return render_template("dashboard.html", items=items)
        else:
            # Optionally handle failed login
            flash("Invalid username or password", "danger")

    return render_template("adminLoginPage.html", form=form)



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("index.html")

@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

