from flask import request, jsonify
from flask_restful import Resource
from flask_login import login_user, logout_user, current_user,login_required
from package.Models import Users
from package import api
from package import db

class login(Resource):
    def post(self):
        creds = request.get_json()
        user=Users.query.filter_by(user_name=creds['user_name']).first()
        if user:
            if user.password == creds['password']:
                #handles user login using User class instance created above
                login_user(user)
                return  jsonify(user_name=creds['user_name'], status = "logged_in")
        return jsonify(message = "username or password is wrong")


class logout(Resource):
    @login_required
    def post(self):
        temp_user = current_user.user_name
        logout_user()
        return jsonify(status = 'logged_out',user_name = temp_user)

class signup(Resource):
    def post(self):
        if current_user.is_authenticated:
            return jsonify(message = 'You are already logged in!')
        user_json = request.get_json()
        new_user = Users(user_name=user_json['user_name'], password=user_json['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(status='added')


class check(Resource):
    def post(self):
        if current_user.is_authenticated:
            return jsonify(logged_in_as = current_user.user_name)
        return jsonify(status = "logged_out")


class users(Resource):
    @login_required
    def post(self):
        output = dict()
        user=Users.query.with_entities(Users.user_id,Users.user_name)
        for index, data in enumerate(user,start=1):
            temp = {'username':data.user_name,'user_id':data.user_id}
            output[index]=temp
        return jsonify(output)
api.add_resource(login,'/', '/login')
api.add_resource(logout,'/logout')
api.add_resource(signup,'/signup')
api.add_resource(check, '/check')
api.add_resource(users, '/users')

