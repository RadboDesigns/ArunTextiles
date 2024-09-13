from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __str__(self):
        return '<Admin %r>' % Admin.id
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return True
    
    def get_id(self):
        return str(self.id)
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    lastname = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    cart_items = db.relationship('Cart', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def __repr__(self):
        return f'<User  {self.id}>' 

class Instagram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_picture = db.Column(db.String(1000), nullable=False)



    def __str__(self):
        return '<Product %r>' % self.product_picture

class BaseProduct(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    about_product = db.Column(db.String(1000), nullable=False)
    single_product_price = db.Column(db.Float, nullable=False)
    brand_name = db.Column(db.String(50), nullable=False)
    no_of_products = db.Column(db.Integer, nullable=False)
    no_of_products_price = db.Column(db.Float, nullable=False)

    product_sizes_no_for_m = db.Column(db.Integer, nullable=True)
    product_sizes_no_for_s = db.Column(db.Integer, nullable=True)
    product_sizes_no_for_l = db.Column(db.Integer, nullable=True)
    product_sizes_no_for_xl = db.Column(db.Integer, nullable=True)
    product_sizes_no_for_xxl = db.Column(db.Integer, nullable=True)
    
    product_code = db.Column(db.String(50), nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_picture_zoom = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)
    certian_number_products = db.Column(db.Integer, nullable=True)
    certian_number_products_discount = db.Column(db.Integer, nullable=True)
    
    @declared_attr
    def __mapper_args__(cls):
        return {
            'polymorphic_on': cls.product_type,
            'polymorphic_identity': cls.__name__
        }

class Product(BaseProduct):
    product_type = db.Column(db.String(50))

    def __str__(self):
        return f'<Product {self.product_name}>' 

class BestSeller(BaseProduct):
    product_type = db.Column(db.String(50))

    def __str__(self):
        return f'<BestSeller {self.product_name}>'

class BestOffers(BaseProduct):
    product_type = db.Column(db.String(50))

    def __str__(self):
        return f'<BestOffers {self.product_name}>'

class ProductPage(BaseProduct):
    product_type = db.Column(db.String(50))

    def __str__(self):
        return f'<ProductPage {self.product_name}>'

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    user_link = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_link_id = db.Column(db.Integer, nullable=False)
    product_link_type = db.Column(db.String(50), nullable=False)  # To identify product type

    __table_args__ = (db.UniqueConstraint('user_link', 'product_link_id', 'product_link_type', name='_user_product_uc'),)
    
    def __str__(self):
        return f'<Cart {self.id}>' 

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    payment_id = db.Column(db.String(50), nullable=False)

    user_link = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_link_id = db.Column(db.Integer, nullable=False)
    product_link_type = db.Column(db.String(50), nullable=False)  # To identify product type

    def __str__(self):
        return f'<Order {self.id}>'
