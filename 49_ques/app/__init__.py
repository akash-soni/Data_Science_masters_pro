from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://akash200287:akash200287@cluster0.4bhfygp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
app.config['SECRET_KEY'] = 'hidden'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)

from app import routes
