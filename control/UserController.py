from flask import redirect, url_for, request, jsonify
from models.User import Usuarios
from control.MainController import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token
from bcrypt import hashpw, gensalt, checkpw


@jwt_required()
def users():
    usuarios = Usuarios.query.all()
    return jsonify([e.serialize for e in usuarios])


def checarUsuarios():
    try:
        email = request.json['email']
        senha = request.json['senha'].encode('utf-8')
        resposta = Usuarios.query.filter_by(email=email).first()
        if resposta:
            if checkpw(senha, resposta.senha.encode('utf-8')):
                access_token = create_access_token(identity=resposta.id)
                return jsonify({'status': 'success', 'id': resposta.id, 'nome': resposta.nome,
                                'access_token': access_token})
            else:
                return jsonify({'status': 'fail', 'msg': 'Senha incorreta'})
        else:
            return jsonify({'status': 'fail', 'msg': 'Email não cadastrado'})
    except Exception as e:
        print(e)


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
