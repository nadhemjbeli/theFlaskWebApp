# import blueprint as blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin


import mysql.connector
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='testflask')
app = Flask(__name__)
# * sqlite:///test.db in a case of SQLlite database
# TODO : Cearte the database testFlask first without structure
# ! Only the name
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/testFlask'
# app.config['WTF_CSRF_SECRET_KEY'] = 'random key for form'
db = SQLAlchemy(app)

app.secret_key = 'some_random_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

import my_app.auth.views as views
admin = Admin(app, index_view=views.MyAdminIndexView())
admin.add_view(views.UserAdminView(views.User, db.session))

from my_app.auth.views import auth
app.register_blueprint(auth)

db.create_all()

app.config["FACEBOOK_OAUTH_CLIENT_ID"] = '410062293565019'
app.config["FACEBOOK_OAUTH_CLIENT_SECRET"] = 'a565dd5291a92607721f62aa4ef44c87'
from my_app.auth.views import facebook_blueprint
app.register_blueprint(facebook_blueprint)

app.config["GOOGLE_OAUTH_CLIENT_ID"] = "602943886498-bj17e83b4q1jfk7kouf3sbsb7ihgpo2i.apps.googleusercontent.com"
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = "77Tx7u3oXGfYNQAURXYXsyPG"
app.config["OAUTHLIB_RELAX_TOKEN_SCOPE"] = True
from my_app.auth.views import google_blueprint
app.register_blueprint(google_blueprint)
