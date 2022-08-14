from package import app
import urllib

class Configs:
    def set_db():
        psswrd = urllib.parse.quote_plus('Arts@14008')
        dbs = 'postgresql://admin:'+psswrd+'@db/user_authentication'
        app.config['SQLALCHEMY_DATABASE_URI']=dbs
    def set_secret():
        app.config['SECRET_KEY']='mysecret'
