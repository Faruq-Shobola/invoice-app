from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES, configure_uploads
from invoice.config import Config
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
image = UploadSet('images', IMAGES)
login_manager.login_view = 'auth.signin'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    configure_uploads(app, image)
    
    

    from .auth.routes import auth
    from .account.routes import acct
    from .client.routes import client
    from .invoice.routes import invoice

    app.register_blueprint(auth)
    app.register_blueprint(acct)
    app.register_blueprint(client, url_prefix='/client')
    app.register_blueprint(invoice, url_prefix='/invoice')

    return app
