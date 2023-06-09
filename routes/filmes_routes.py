from flask import Blueprint
from control.FilmesController import consultarFilmes

filmes_routes = Blueprint('filmes_routes', __name__)

filmes_routes.route('/filmes', methods=['GET', 'POST'])(consultarFilmes)
