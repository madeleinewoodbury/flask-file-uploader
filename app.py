import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
db = SQLAlchemy()

app.config['SECRET_KEY'] = os.getenv('SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['UPLOAD_FOLDER'] = 'images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


db.init_app(app)

from auth import auth
from routes import routes
app.register_blueprint(routes)
app.register_blueprint(auth)

migrate = Migrate(app, db)
import models

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(id)


