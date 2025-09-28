from flask import Flask
from flask_migrate import Migrate
from app.extensions import db, lm
from flask_bcrypt import Bcrypt
from app.models import Users
from datetime import timedelta
from dotenv import load_dotenv
from os import environ
  



def connectAidApp():
    load_dotenv()
    app = Flask(__name__, template_folder="../templates", static_folder='../static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///connectaid_db.db'
    app.config['SECRET_KEY'] =environ.get("SECRET_KEY")
    app.config['SECURITY_PASSWORD_SALT'] =environ.get("SECURITY_PASSWORD_SALT") 
    app.config['PASSWORD_RESET_TIMEOUT'] = 3600 
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'oscarlance20@gmail.com'
    app.config['MAIL_PASSWORD'] =environ.get('GMAIL_APP_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = 'ConnectAid <noreply@connectaid.org>'



    
    db.init_app(app)
    lm.init_app(app)
    
    

    @lm.user_loader
    def loadUser(id):
        return Users.query.get(id)
    
    from app.routes import routesManager
    encrypt=Bcrypt(app)
    routesManager(app, db, encrypt)

    migrate = Migrate(app,db)

    def format_datetime(value, format='%b %d, %Y'):
        if value is None:
            return ""
        return value.strftime(format)

    app.jinja_env.filters['datetimeformat'] = format_datetime


    return app

__all__=['db', 'lm', 'connectAidApp']