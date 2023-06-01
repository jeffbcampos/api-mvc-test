from flask import Blueprint
from control.UserController import cadastro, users

users_routes = Blueprint('users_routes', __name__)

users_routes.route('/users', methods=['GET', 'POST'])(users)
users_routes.route('/cadastro', methods=['POST'])(cadastro)
