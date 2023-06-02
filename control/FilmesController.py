from flask import redirect, url_for, request, jsonify
from models.Filmes import Filmes
from control.MainController import db


def consultarFilmes():
    filmes = Filmes.query.all()
    return jsonify([e.serialize for e in filmes])
