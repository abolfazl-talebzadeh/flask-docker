from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

from package import views
from package import Models
from package import login_manager
from package.config import Configs

Configs.set_db()
Configs.set_secret()