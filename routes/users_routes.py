from flask import Blueprint
from control.UserController import cadastro, users, checarUsuarios

users_routes = Blueprint('users_routes', __name__)

users_routes.route('/users', methods=['GET'])(users)
users_routes.route('/cadastro', methods=['POST'])(cadastro)
users_routes.route('/usuarios', methods=['POST'])(checarUsuarios)
