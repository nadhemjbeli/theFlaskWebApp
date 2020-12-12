from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin


import mysql.connector
#cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='testflask')
app = Flask(__name__)
# * sqlite:///test.db in a case of SQLlite database
# TODO : Cearte the database testFlask first without structure
# ! Only the name
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testFlask'
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
