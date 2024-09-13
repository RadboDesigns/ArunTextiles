
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField,TextAreaField, SubmitField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, length, NumberRange, Email
from flask_wtf.file import FileField, FileRequired


class PaymentForm(FlaskForm):
    amount = HiddenField('Amount', validators=[DataRequired()])
    purpose = HiddenField('Purpose', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])


class CartForm(FlaskForm):
    submit = SubmitField('Remove from Cart')
    
class DummyForm(FlaskForm):
    pass

class UserProfileUpdateForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Update')


class UserSigupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    user_name = StringField('User Name', validators=[DataRequired()])
    password_1 = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    password_2 = PasswordField('Confirm Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Submit & Register')
    
class AdminLoginForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')

class ShopItemsForm(FlaskForm):
    choices = [('all', 'All Products'), ('newBorn', 'New Born'), ('kids', 'Kids'), ('boys', 'Boys'), ('girls', 'Girls'), ('men', 'Men'), ('women', 'Woman')]

    product_name = StringField('Name of Product', validators=[DataRequired()])
    about_product = TextAreaField('About Product', validators=[DataRequired()])
    single_product_price = FloatField('Single Piece Price', validators=[DataRequired()])
    brand_name = StringField('Brand Name', validators=[DataRequired()])
    no_of_products = IntegerField('Number of Products', validators=[DataRequired(), NumberRange(min=1, max=100)])
    no_of_products_price = FloatField('Number of Products Price', validators=[DataRequired()])

    product_sizes_no_for_m = IntegerField('Number of Products from M', validators=[DataRequired(), NumberRange(min=0, max=100)])
    product_sizes_no_for_s = IntegerField('Number of Products from S', validators=[DataRequired(), NumberRange(min=0, max=100)])
    product_sizes_no_for_l = IntegerField('Number of Products from L', validators=[DataRequired(), NumberRange(min=0, max=100)])
    product_sizes_no_for_xl = IntegerField('Number of Products from XL', validators=[DataRequired(), NumberRange(min=0, max=100)])
    product_sizes_no_for_xxl = IntegerField('Number of Products from XXL', validators=[DataRequired(), NumberRange(min=0, max=100)])

    product_code = StringField('Product Code', validators=[DataRequired()])
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    product_picture_zoom = FileField('Zoom Picture', validators=[DataRequired()])
    product_tag = SelectMultipleField('Product Filter', choices=choices, validators=[DataRequired()])
    certian_number_products = IntegerField('Certain Number of Products', validators=[DataRequired(), NumberRange(min=0, max=100)])
    certian_number_products_discount = IntegerField('Certain Number of Products Discount', validators=[DataRequired(), NumberRange(min=0, max=100)])

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')



class InstaForm(FlaskForm):
    product_picture = FileField('Product Picture', validators=[DataRequired()])
    
    add_product = SubmitField('Add Product')



