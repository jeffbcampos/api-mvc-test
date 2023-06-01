from flask import Blueprint
from control.UserController import cadastro, users

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['GET', 'POST'])(users)
user_bp.route('/cadastro', methods=['POST'])(cadastro)
