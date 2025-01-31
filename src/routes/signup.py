from flask import Blueprint, request, jsonify
from models.users import Usuarios
from models import db
from routes.sessions import current_session
from werkzeug.security import generate_password_hash

signup = Blueprint('signup', __name__)

@signup.route('/', methods=['POST'])
def signup_regist():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        mail = data.get('mail')

        if not username or not password:
            return jsonify({"message": "Missing username or password"}), 400

        if Usuarios.query.filter_by(username=username).first() or Usuarios.query.filter_by(mail=mail).first():
            return jsonify({"message": "User already exists"}), 400

        new_user = Usuarios(
            username=username,
            password_hash=generate_password_hash(password),
            authenticated=False,
            mail=mail
        )

        db.session.add(new_user)
        db.session.commit()
        current_session['user_id'] = new_user.id
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"message": "Server error", "error": str(e)}), 500