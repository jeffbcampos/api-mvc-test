from flask import redirect, url_for, request, jsonify
from models.User import Usuarios
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def users():
    query = Usuarios.query.all()
    return jsonify([e.serialize for e in query])


def cadastro():
    nome = request.json['nome']
    email = request.json['email']
    senha = request.json['senha']
    usuario = Usuarios(nome=nome, email=email, senha=senha)
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.serialize)
