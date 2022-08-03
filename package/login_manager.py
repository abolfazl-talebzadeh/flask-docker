from flask_login import LoginManager
from package import app
from package.Models import Users


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ""

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

