from flask import Blueprint
from control.UserController import cadastro, users, checarUsuarios, atualizarUsuario, atualizarSenha, inserirUsuario

users_routes = Blueprint('users_routes', __name__)

users_routes.route('/users', methods=['GET'])(users)
users_routes.route('/cadastro', methods=['POST'])(cadastro)
users_routes.route('/usuarios', methods=['POST'])(checarUsuarios)
users_routes.route('/atualizarUsuario', methods=['POST'])(atualizarUsuario)
users_routes.route('/atualizarSenha', methods=['POST'])(atualizarSenha)
users_routes.route('/inserirUsuario', methods=['POST'])(inserirUsuario)
