from flask import Flask
from flask_cors import CORS
from models import db


def create_app():
    app = Flask(__name__, static_folder = 'views', static_url_path='')
    app.debug = True
    app.secret_key = "key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:userpassword@mysql/mydatabase'
    CORS(app, resources={r"/auth/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS", "PUT"], "supports_credentials": True}})
    db.init_app(app)
    CORS(app)
    from routes.signup import signup
    from routes.login import login
    from routes.signout import signout

    with app.app_context():
        db.create_all()
    
    app.register_blueprint(signup, url_prefix='/auth')
    app.register_blueprint(login, url_prefix='/auth')
    app.register_blueprint(signout, url_prefix='/auth')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)