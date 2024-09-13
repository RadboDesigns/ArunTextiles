from flask import Blueprint, render_template, flash, send_from_directory, redirect, session, request, url_for
from .forms import ShopItemsForm, InstaForm
from werkzeug.utils import secure_filename
from .models import Product, BestSeller, BestOffers, Instagram, ProductPage
from . import db
from flask_login import login_required

admin = Blueprint('admin', __name__)


@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory('../media', filename)


@admin.route('/best_sellers/<path:filename>')
def get_bestseller(filename):
    return send_from_directory('../best_sellers', filename)


@admin.route('/dash_bestoffers/<path:filename>')
def get_bestoffers(filename):
    return send_from_directory('../dash_bestoffers', filename)


@admin.route('/dash_insta/<path:filename>')
def get_insta(filename):
    return send_from_directory('../dash_insta', filename)

@admin.route('/product/<path:filename>')
def get_product(filename):
    return send_from_directory('../product', filename)


@admin.route('/add-get_bestoffers-items', methods=['GET', 'POST'])
@login_required
def add_get_bestoffers_items():
    form = ShopItemsForm()

    if form.validate_on_submit():
        product_name = form.product_name.data
        about_product = form.about_product.data
        single_product_price = form.single_product_price.data
        brand_name = form.brand_name.data
        no_of_products = form.no_of_products.data
        no_of_products_price = form.no_of_products_price.data
        product_code = form.product_code.data
        certian_number_products = form.certian_number_products.data
        certian_number_products_discount = form.certian_number_products_discount.data

        product_sizes_no_for_m = request.form.get('product_sizes_no_for_m')
        product_sizes_no_for_s = request.form.get('product_sizes_no_for_s')
        product_sizes_no_for_l = request.form.get('product_sizes_no_for_l')
        product_sizes_no_for_xl = request.form.get('product_sizes_no_for_xl')
        product_sizes_no_for_xxl = request.form.get('product_sizes_no_for_xxl')

        product_tag = form.product_tag.data

        file = form.product_picture.data
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'
        file.save(file_path)

        file_zoom = form.product_picture_zoom.data
        file_name_zoom = secure_filename(file_zoom.filename)
        file_path_zoom = f'./media/{file_name_zoom}'
        file_zoom.save(file_path_zoom)

        new_shop_item = BestOffers(
            product_name=product_name,
            about_product=about_product,
            single_product_price=single_product_price,
            brand_name=brand_name,
            no_of_products=no_of_products,
            no_of_products_price=no_of_products_price,
            product_code=product_code,
            certian_number_products=certian_number_products,
            certian_number_products_discount=certian_number_products_discount,
            product_sizes_no_for_m=product_sizes_no_for_m,
            product_sizes_no_for_s=product_sizes_no_for_s,
            product_sizes_no_for_l=product_sizes_no_for_l,
            product_sizes_no_for_xl=product_sizes_no_for_xl,
            product_sizes_no_for_xxl=product_sizes_no_for_xxl,
            product_tag=','.join(product_tag),
            product_picture=file_path,
            product_picture_zoom=file_path_zoom
        )
        
        try:
            db.session.add(new_shop_item)
            db.session.commit()
            flash(f'{product_name} added Successfully')
            print('Product Added')
            return redirect(url_for('admin.shop_items'))
        except Exception as e:
            print(f'Error: {e}')
            flash('Product Not Added!!')

    print(form.errors)
    return render_template('add_shop_items.html', form=form)


@admin.route('/add_best_sellers_items', methods=['GET', 'POST'])
@login_required
def add_best_sellers_items():
    form = ShopItemsForm()

    if form.validate_on_submit():
        product_name = form.product_name.data
        about_product = form.about_product.data
        single_product_price = form.single_product_price.data
        brand_name = form.brand_name.data
        no_of_products = form.no_of_products.data
        no_of_products_price = form.no_of_products_price.data
        product_code = form.product_code.data
        certian_number_products = form.certian_number_products.data
        certian_number_products_discount = form.certian_number_products_discount.data

        product_sizes_no_for_m = request.form.get('product_sizes_no_for_m')
        product_sizes_no_for_s = request.form.get('product_sizes_no_for_s')
        product_sizes_no_for_l = request.form.get('product_sizes_no_for_l')
        product_sizes_no_for_xl = request.form.get('product_sizes_no_for_xl')
        product_sizes_no_for_xxl = request.form.get('product_sizes_no_for_xxl')

        product_tag = form.product_tag.data

        file = form.product_picture.data
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'
        file.save(file_path)

        file_zoom = form.product_picture_zoom.data
        file_name_zoom = secure_filename(file_zoom.filename)
        file_path_zoom = f'./media/{file_name_zoom}'
        file_zoom.save(file_path_zoom)

        new_shop_item = BestSeller(
            product_name=product_name,
            about_product=about_product,
            single_product_price=single_product_price,
            brand_name=brand_name,
            no_of_products=no_of_products,
            no_of_products_price=no_of_products_price,
            product_code=product_code,
            certian_number_products=certian_number_products,
            certian_number_products_discount=certian_number_products_discount,
            product_sizes_no_for_m=product_sizes_no_for_m,
            product_sizes_no_for_s=product_sizes_no_for_s,
            product_sizes_no_for_l=product_sizes_no_for_l,
            product_sizes_no_for_xl=product_sizes_no_for_xl,
            product_sizes_no_for_xxl=product_sizes_no_for_xxl,
            product_tag=','.join(product_tag),
            product_picture=file_path,
            product_picture_zoom=file_path_zoom
        )
        
        try:
            db.session.add(new_shop_item)
            db.session.commit()
            flash(f'{product_name} added Successfully')
            print('Product Added')
            return redirect(url_for('admin.shop_items'))
        except Exception as e:
            print(f'Error: {e}')
            flash('Product Not Added!!')

    print(form.errors)
    return render_template('add_shop_items.html', form=form)

@admin.route('/add-dash_insta-items', methods=['GET', 'POST'])
def add_dash_insta_items():
    form = InstaForm()

    if form.validate_on_submit():

        file = form.product_picture.data

        file_name = secure_filename(file.filename)

        file_path = f'./dash_insta/{file_name}'

        file.save(file_path)

        new_shop_item = Instagram()

        new_shop_item.product_picture = file_path

        try:
            db.session.add(new_shop_item)
            db.session.commit()
            flash(f'{file_name} added Successfully')
            print('Product Added')
            return render_template('add_dash_insta_items.html', form=form)
        except Exception as e:
            print(e)
            flash('Product Not Added!!')

    return render_template('add_dash_insta_items.html', form=form)


@admin.route('/add-dash_insta-items', methods=['GET', 'POST'])
@login_required
def add_dash_product_items():
    form = ShopItemsForm()

    if form.validate_on_submit():
        product_name = form.product_name.data
        about_product = form.about_product.data
        single_product_price = form.single_product_price.data
        brand_name = form.brand_name.data
        no_of_products = form.no_of_products.data
        no_of_products_price = form.no_of_products_price.data
        product_code = form.product_code.data
        certian_number_products = form.certian_number_products.data
        certian_number_products_discount = form.certian_number_products_discount.data

        product_sizes_no_for_m = request.form.get('product_sizes_no_for_m')
        product_sizes_no_for_s = request.form.get('product_sizes_no_for_s')
        product_sizes_no_for_l = request.form.get('product_sizes_no_for_l')
        product_sizes_no_for_xl = request.form.get('product_sizes_no_for_xl')
        product_sizes_no_for_xxl = request.form.get('product_sizes_no_for_xxl')

        product_tag = form.product_tag.data

        file = form.product_picture.data
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'
        file.save(file_path)

        file_zoom = form.product_picture_zoom.data
        file_name_zoom = secure_filename(file_zoom.filename)
        file_path_zoom = f'./media/{file_name_zoom}'
        file_zoom.save(file_path_zoom)

        new_shop_item = ProductPage(
            product_name=product_name,
            about_product=about_product,
            single_product_price=single_product_price,
            brand_name=brand_name,
            no_of_products=no_of_products,
            no_of_products_price=no_of_products_price,
            product_code=product_code,
            certian_number_products=certian_number_products,
            certian_number_products_discount=certian_number_products_discount,
            product_sizes_no_for_m=product_sizes_no_for_m,
            product_sizes_no_for_s=product_sizes_no_for_s,
            product_sizes_no_for_l=product_sizes_no_for_l,
            product_sizes_no_for_xl=product_sizes_no_for_xl,
            product_sizes_no_for_xxl=product_sizes_no_for_xxl,
            product_tag=','.join(product_tag),
            product_picture=file_path,
            product_picture_zoom=file_path_zoom
        )
        
        try:
            db.session.add(new_shop_item)
            db.session.commit()
            flash(f'{product_name} added Successfully')
            print('Product Added')
            return redirect(url_for('admin.shop_items'))
        except Exception as e:
            print(f'Error: {e}')
            flash('Product Not Added!!')

    print(form.errors)
    return render_template('add_shop_items.html', form=form)



@admin.route('/add-shop-items', methods=['GET', 'POST'])
@login_required
def add_shop_items():
    form = ShopItemsForm()

    if form.validate_on_submit():
        product_name = form.product_name.data
        about_product = form.about_product.data
        single_product_price = form.single_product_price.data
        brand_name = form.brand_name.data
        no_of_products = form.no_of_products.data
        no_of_products_price = form.no_of_products_price.data
        product_code = form.product_code.data
        certian_number_products = form.certian_number_products.data
        certian_number_products_discount = form.certian_number_products_discount.data

        product_sizes_no_for_m = request.form.get('product_sizes_no_for_m')
        product_sizes_no_for_s = request.form.get('product_sizes_no_for_s')
        product_sizes_no_for_l = request.form.get('product_sizes_no_for_l')
        product_sizes_no_for_xl = request.form.get('product_sizes_no_for_xl')
        product_sizes_no_for_xxl = request.form.get('product_sizes_no_for_xxl')

        product_tag = form.product_tag.data

        file = form.product_picture.data
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'
        file.save(file_path)

        file_zoom = form.product_picture_zoom.data
        file_name_zoom = secure_filename(file_zoom.filename)
        file_path_zoom = f'./media/{file_name_zoom}'
        file_zoom.save(file_path_zoom)

        new_shop_item = Product(
            product_name=product_name,
            about_product=about_product,
            single_product_price=single_product_price,
            brand_name=brand_name,
            no_of_products=no_of_products,
            no_of_products_price=no_of_products_price,
            product_code=product_code,
            certian_number_products=certian_number_products,
            certian_number_products_discount=certian_number_products_discount,
            product_sizes_no_for_m=product_sizes_no_for_m,
            product_sizes_no_for_s=product_sizes_no_for_s,
            product_sizes_no_for_l=product_sizes_no_for_l,
            product_sizes_no_for_xl=product_sizes_no_for_xl,
            product_sizes_no_for_xxl=product_sizes_no_for_xxl,
            product_tag=','.join(product_tag),
            product_picture=file_path,
            product_picture_zoom=file_path_zoom
        )
        
        try:
            db.session.add(new_shop_item)
            db.session.commit()
            flash(f'{product_name} added Successfully')
            print('Product Added')
            return redirect(url_for('admin.shop_items'))
        except Exception as e:
            print(f'Error: {e}')
            flash('Product Not Added!!')

    print(form.errors)
    return render_template('add_shop_items.html', form=form)




@admin.route('/update_product/<int:product_id>', methods=['POST'])
@login_required
def update_product(product_id):
    # Retrieve form data
    product_picture = request.form.get('product_picture')
    product_picture_zoom = request.form.get('product_picture_zoom')
    product_name = request.form.get('product_name')
    about_product = request.form.get('about_product')
    single_product_price = request.form.get('single_product_price')
    brand_name = request.form.get('brand_name')
    no_of_products = request.form.get('no_of_products')
    no_of_products_price = request.form.get('no_of_products_price')
    product_code = request.form.get('product_code')
    product_tag = request.form.get('product_tag')
    product_sizes_no_for_s = request.form.get('product_sizes_no_for_s')
    product_sizes_no_for_m = request.form.get('product_sizes_no_for_m')
    product_sizes_no_for_l = request.form.get('product_sizes_no_for_l')
    product_sizes_no_for_xl = request.form.get('product_sizes_no_for_xl')
    product_sizes_no_for_xxl = request.form.get('product_sizes_no_for_xxl')
    certian_number_products = request.form.get('certian_number_products')
    certian_number_products_discount = request.form.get('certian_number_products_discount')

    # Update the Product model
    product = Product.query.get(product_id)
    if product:
        product.product_picture = product_picture
        product.product_picture_zoom = product_picture_zoom
        product.product_name = product_name
        product.about_product = about_product
        product.single_product_price = single_product_price
        product.brand_name = brand_name
        product.no_of_products = no_of_products
        product.no_of_products_price = no_of_products_price
        product.product_code = product_code
        product.product_tag = product_tag
        product.product_sizes_no_for_s = product_sizes_no_for_s
        product.product_sizes_no_for_m = product_sizes_no_for_m
        product.product_sizes_no_for_l = product_sizes_no_for_l
        product.product_sizes_no_for_xl = product_sizes_no_for_xl
        product.product_sizes_no_for_xxl = product_sizes_no_for_xxl
        product.certian_number_products = certian_number_products
        product.certian_number_products_discount = certian_number_products_discount

        db.session.commit()
        flash('Product updated successfully', 'success')
    else:
        flash('Product not found', 'error')

    # Update the ProductPage model
    product_page = ProductPage.query.get(product_id)
    if product_page:
        product.product_picture = product_picture
        product.product_picture_zoom = product_picture_zoom
        product.product_name = product_name
        product.about_product = about_product
        product.single_product_price = single_product_price
        product.brand_name = brand_name
        product.no_of_products = no_of_products
        product.no_of_products_price = no_of_products_price
        product.product_code = product_code
        product.product_tag = product_tag
        product.product_sizes_no_for_s = product_sizes_no_for_s
        product.product_sizes_no_for_m = product_sizes_no_for_m
        product.product_sizes_no_for_l = product_sizes_no_for_l
        product.product_sizes_no_for_xl = product_sizes_no_for_xl
        product.product_sizes_no_for_xxl = product_sizes_no_for_xxl
        product.certian_number_products = certian_number_products
        product.certian_number_products_discount = certian_number_products_discount

        db.session.commit()
        flash('ProductPage updated successfully', 'success')
    else:
        flash('ProductPage not found', 'error')

    # Update the BestSeller model
    best_seller = BestSeller.query.get(product_id)
    if best_seller:
        product.product_picture = product_picture
        product.product_picture_zoom = product_picture_zoom
        product.product_name = product_name
        product.about_product = about_product
        product.single_product_price = single_product_price
        product.brand_name = brand_name
        product.no_of_products = no_of_products
        product.no_of_products_price = no_of_products_price
        product.product_code = product_code
        product.product_tag = product_tag
        product.product_sizes_no_for_s = product_sizes_no_for_s
        product.product_sizes_no_for_m = product_sizes_no_for_m
        product.product_sizes_no_for_l = product_sizes_no_for_l
        product.product_sizes_no_for_xl = product_sizes_no_for_xl
        product.product_sizes_no_for_xxl = product_sizes_no_for_xxl
        product.certian_number_products = certian_number_products
        product.certian_number_products_discount = certian_number_products_discount

        db.session.commit()
        flash('BestSeller updated successfully', 'success')
    else:
        flash('BestSeller not found', 'error')

    return redirect(url_for('admin.dash_product'))



@admin.route('/shop-items', methods=['GET', 'POST'])
@login_required
def shop_items():
    items = Product.query.order_by(Product.id).all()
    return render_template('shop_items.html', items=items)

@admin.route('/shop-bestselle', methods=['GET', 'POST'])
@login_required
def dash_bestseller():
    items = BestSeller.query.order_by(BestSeller.id).all()
    return render_template('dash_bestseller.html', items_bestSeller=items)

@admin.route('/shop-bestoffers', methods=['GET', 'POST'])
@login_required
def dash_bestoffers():
    items = BestOffers.query.order_by(BestOffers.id).all()
    return render_template('dash_bestoffers.html', items_bestOffer=items)

@admin.route('/shop-insta', methods=['GET', 'POST'])
@login_required
def dash_insta():
    items = Instagram.query.order_by(Instagram.id).all()
    return render_template('dash_insta.html', items_insta=items)

@admin.route('/shop-product', methods=['GET', 'POST'])
@login_required
def dash_product():
    items = ProductPage.query.order_by(ProductPage.id).all()
    return render_template('dash_product.html', items_product=items)




@admin.route('/update-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):

    item_to_update = Product.query.get(item_id)

    if request.method == 'POST':
        if item_to_update:
            item_to_update.product_name = request.form['product_name']
            item_to_update.about_product = request.form['about_product']
            item_to_update.single_product_price = request.form['single_product_price']
            item_to_update.brand_name = request.form['brand_name']
            item_to_update.no_of_products = request.form['no_of_products']
            item_to_update.no_of_products_price = request.form['no_of_products_price']

            item_to_update.product_sizes_no_for_m = request.form['product_sizes_no_for_m']
            item_to_update.product_sizes_no_for_s = request.form['product_sizes_no_for_s']
            item_to_update.product_sizes_no_for_l = request.form['product_sizes_no_for_l']
            item_to_update.product_sizes_no_for_xl = request.form['product_sizes_no_for_xl']
            item_to_update.product_sizes_no_for_xxl = request.form['product_sizes_no_for_xxl']

            item_to_update.product_code = request.form['product_code']
            item_to_update.product_picture = request.form['product_picture']
            item_to_update.product_tag = request.form['product_tag']
            item_to_update.certian_number_products = request.form['certian_number_products']
            item_to_update.certian_number_products_discount = request.form['certian_number_products_discount']


            
            db.session.commit()
            return redirect(url_for('admin.shop_items'))

    return render_template('update_item.html', item_to_update=item_to_update)










@admin.route('/update-best_sellers-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_best_sellers_item(item_id):

    item_to_update = BestSeller.query.get(item_id)

    if request.method == 'POST':
        if item_to_update:
            item_to_update.product_name = request.form['product_name']
            item_to_update.about_product = request.form['about_product']
            item_to_update.single_product_price = request.form['single_product_price']
            item_to_update.brand_name = request.form['brand_name']
            item_to_update.no_of_products = request.form['no_of_products']
            item_to_update.no_of_products_price = request.form['no_of_products_price']

            item_to_update.product_sizes_no_for_m = request.form['product_sizes_no_for_m']
            item_to_update.product_sizes_no_for_s = request.form['product_sizes_no_for_s']
            item_to_update.product_sizes_no_for_l = request.form['product_sizes_no_for_l']
            item_to_update.product_sizes_no_for_xl = request.form['product_sizes_no_for_xl']
            item_to_update.product_sizes_no_for_xxl = request.form['product_sizes_no_for_xxl']

            item_to_update.product_code = request.form['product_code']
            item_to_update.product_picture = request.form['product_picture']
            item_to_update.product_tag = request.form['product_tag']
            item_to_update.certian_number_products = request.form['certian_number_products']
            item_to_update.certian_number_products_discount = request.form['certian_number_products_discount']


            db.session.commit()
            return redirect(url_for('admin.dash_bestseller'))

    return render_template('update_best_sellers_item.html', item_to_update=item_to_update)


@admin.route('/update-get_bestoffers-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_get_bestoffers_item(item_id):

    item_to_update = BestOffers.query.get(item_id)

    if request.method == 'POST':
        if item_to_update:
            item_to_update.product_name = request.form['product_name']
            item_to_update.about_product = request.form['about_product']
            item_to_update.single_product_price = request.form['single_product_price']
            item_to_update.brand_name = request.form['brand_name']
            item_to_update.no_of_products = request.form['no_of_products']
            item_to_update.no_of_products_price = request.form['no_of_products_price']

            item_to_update.product_sizes_no_for_m = request.form['product_sizes_no_for_m']
            item_to_update.product_sizes_no_for_s = request.form['product_sizes_no_for_s']
            item_to_update.product_sizes_no_for_l = request.form['product_sizes_no_for_l']
            item_to_update.product_sizes_no_for_xl = request.form['product_sizes_no_for_xl']
            item_to_update.product_sizes_no_for_xxl = request.form['product_sizes_no_for_xxl']

            item_to_update.product_code = request.form['product_code']
            item_to_update.product_picture = request.form['product_picture']
            item_to_update.product_tag = request.form['product_tag']
            item_to_update.certian_number_products = request.form['certian_number_products']
            item_to_update.certian_number_products_discount = request.form['certian_number_products_discount']


            db.session.commit()
            return redirect(url_for('admin.dash_bestoffers'))

    return render_template('update_get_bestoffers_item.html', item_to_update=item_to_update)



@admin.route('/update-dash_product-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_dash_product_item(item_id):


    item_to_update = ProductPage.query.get(item_id)
    if request.method == 'POST':
        if item_to_update:
            item_to_update.product_name = request.form['product_name']
            item_to_update.about_product = request.form['about_product']
            item_to_update.single_product_price = request.form['single_product_price']
            item_to_update.brand_name = request.form['brand_name']
            item_to_update.no_of_products = request.form['no_of_products']
            item_to_update.no_of_products_price = request.form['no_of_products_price']

            item_to_update.product_sizes_no_for_m = request.form['product_sizes_no_for_m']
            item_to_update.product_sizes_no_for_s = request.form['product_sizes_no_for_s']
            item_to_update.product_sizes_no_for_l = request.form['product_sizes_no_for_l']
            item_to_update.product_sizes_no_for_xl = request.form['product_sizes_no_for_xl']
            item_to_update.product_sizes_no_for_xxl = request.form['product_sizes_no_for_xxl']

            item_to_update.product_code = request.form['product_code']
            item_to_update.product_picture = request.form['product_picture']
            item_to_update.product_tag = request.form['product_tag']
            item_to_update.certian_number_products = request.form['certian_number_products']
            item_to_update.certian_number_products_discount = request.form['certian_number_products_discount']

            db.session.commit()
            return redirect(url_for('admin.dash_product'))

    return render_template('update_dash_product_item.html', item_to_update=item_to_update)






@admin.route('/delete-item/<int:item_id>', methods=['GET', 'POST'])
def delete_item(item_id):
    try:
        item_to_delete = ProductPage.query.get(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('One Item deleted')
        return redirect(url_for('admin.shop-product'))
    except Exception as e:
        print('Item not deleted', e)
        flash('Item not deleted!!')
    return redirect(url_for('admin.dash_product'))

@admin.route('/delete-best_sellers-item/<int:item_id>', methods=['GET', 'POST'])
def delete_best_sellers_items(item_id):
    try:
        item_to_delete = BestSeller.query.get(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('One Item deleted')
        return redirect(url_for('admin.shop-bestselle'))
    except Exception as e:
        print('Item not deleted', e)
        flash('Item not deleted!!')
    return redirect(url_for('admin.dash_bestseller'))

@admin.route('/delete-get_bestoffers-item/<int:item_id>', methods=['GET', 'POST'])
def delete_get_bestoffers_items(item_id):
    try:
        item_to_delete = BestOffers.query.get(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('One Item deleted')
        return redirect(url_for('admin.dash_bestoffers'))
    except Exception as e:
        print('Item not deleted', e)
        flash('Item not deleted!!')
    return redirect(url_for('admin.dash_bestoffers'))

@admin.route('/delete-dash_insta-item/<int:item_id>', methods=['GET', 'POST'])
def delete_dash_insta_items(item_id):
    try:
        item_to_delete = Instagram.query.get(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('One Item deleted')
        return redirect(url_for('admin.shop-insta'))
    except Exception as e:
        print('Item not deleted', e)
        flash('Item not deleted!!')
    return redirect(url_for('admin.dash_insta'))


@admin.route('/delete-product-item-product/<int:item_id>', methods=['GET', 'POST'])
def delete_product_item(item_id):
    try:
        item_to_delete = Product.query.get(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('One Item deleted')
        return redirect(url_for('admin.shop_items'))
    except Exception as e:
        print('Item not deleted', e)
        flash('Item not deleted!!')
    return redirect(url_for('admin.dash_product'))









