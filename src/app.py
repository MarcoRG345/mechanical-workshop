from flask import Flask
def create_app():
    app = Flask(__name__, static_folder = 'views', static_url_path='')
    app.debug = True
    app.secret_key = "key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:userpassword@mysql/mydatabase'
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)