from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_user
from flask_wtf.csrf import CSRFProtect
from instamojo_wrapper import Instamojo

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'


def create_database():
    db.create_all()
    print('Database Created')

def delete_database():
    db.drop_all()
    print('DataBase deleted')



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'xxxxyyyyyzzzzz'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    csrf = CSRFProtect(app)
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Product, BestSeller, BestOffers, Instagram, ProductPage, Admin, User


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    with app.app_context():
        create_database()

        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id)) 
        
        # Update User in the model

        # single_user = Admin(username='Arun-Admin', password='Arun@12345')
        # db.session.add(single_user)
        # db.session.commit()
        # print('UserName Add')

    # with app.app_context():
    #     delete_database()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

