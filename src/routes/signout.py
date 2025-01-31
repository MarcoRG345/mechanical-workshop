from routes.sessions import current_session
from flask import Blueprint, jsonify
signout = Blueprint('signout', __name__)

@signout.route('/signout', methods=['POST'])
def singout_me():
    try:
        current_session.pop('user_id', None)
        return jsonify({"message": "closing_session"}), 201
    except Exception as e:
        return jsonify({"message": "server_not_process_data", "response": str(e)}), 500
