from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdatabase.db'

db = SQLAlchemy(app)

asgi_app = WsgiToAsgi(app)
from flaskproject import urls