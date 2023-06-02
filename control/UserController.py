from flask import redirect, url_for, request, jsonify
from models.User import Usuarios
from control.MainController import db


def users():
    usuarios = Usuarios.query.all()
    return jsonify([e.serialize for e in usuarios])


def cadastro():
    nome = request.json['nome']
    email = request.json['email']
    senha = request.json['senha']
    usuario = Usuarios(nome=nome, email=email, senha=senha)
    result = Usuarios.query.filter_by(email=email).first()
    print(result.email)
    if result:
        return jsonify({'msg': 'Email já cadastrado'})
    else:
        db.session.add(usuario)
        db.session.commit()
        return jsonify(usuario.serialize)
