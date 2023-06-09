from flask import redirect, url_for, request, jsonify
from models.Filmes import Filmes
from control.MainController import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token


@jwt_required()
def consultarFilmes():
    try:
        if request.method == 'GET':
            id = get_jwt_identity()
            response = Filmes.query.filter_by(id_usuario=id).all()
            return jsonify([e.serialize for e in response])
        elif request.method == 'POST':
            titulo = request.json['titulo']
            id_usuario = get_jwt_identity()
            response = Filmes.query.filter_by(titulo=titulo,id_usuario=id_usuario).first()
            if response:
                return jsonify({'msg': 'success'})
            else:
                return jsonify({'msg': 'fail'})
    except Exception as e:
        print(e)
