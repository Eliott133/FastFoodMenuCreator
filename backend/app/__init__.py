from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config as CONFIG

# Extensions initialisation
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config['SECRET_KEY'] = CONFIG.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG.DATABASE_URI

    # Initializing Extensions with Flask App
    db.init_app(app)

    # Save blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app