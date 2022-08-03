from flask_login import UserMixin
from package import db

#creating database class
class Users(UserMixin,db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String())
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    def __repr__(self):
        return f"<User {self.user_name}>"
    def get_id(self):
        # returns the user e-mail
        return (self.user_id)