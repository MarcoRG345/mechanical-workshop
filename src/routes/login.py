from routes.sessions import current_session
from models.users import Usuarios
from flask import jsonify, request, Blueprint
from models import db

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_me():
    try:
        requestJSON = request.get_json()
        current_username = requestJSON.get('username')
        current_password = requestJSON.get('password')
        in_db_user = db.session.execute(
            db.select(Usuarios).where(Usuarios.username == current_username)
        ).scalar_one_or_none()
        if not in_db_user or not in_db_user.check_password(current_password):
            return jsonify({"message": "no_permission", "response": "user_not_found_or_invalid_fields"}), 400
        current_session['user_id'] = in_db_user.get_id()
        return jsonify({"message": "authorized", "response": "success"}), 201
    except Exception as e:
        return jsonify({"message": "server_not_process_data", "response": str(e)}), 500