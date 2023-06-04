from flask import redirect, url_for, request, jsonify
from models.User import Usuarios
from control.MainController import db, verificaSenha
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token
from bcrypt import hashpw, gensalt, checkpw
from routes.mail_routes import mail_routes


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

@jwt_required()
def atualizarUsuario():
    try:
        nome = request.json['nome']
        senha = request.json['senha'].encode('utf-8')
        id_usuario = get_jwt_identity()
        response = Usuarios.query.filter_by(id=id_usuario).first()
        if checkpw(senha, response.senha.encode('utf-8')):
            update = update(Usuarios).where(Usuarios.id == id_usuario).values(nome=nome)
            db.execute(update)
            db.commit()
            return jsonify({'status': 'success', 'msg': 'Usuário atualizado com sucesso'})
        else:
            return jsonify({'status': 'fail', 'msg': 'Senha incorreta'})
    except Exception as e:
        print(e)
        
        
@jwt_required()
def atualizarSenha():
    try:
        senhaAtual = request.json['senhaAtual'].encode('utf-8')
        senha = request.json['senha'].encode('utf-8')
        id_usuario = get_jwt_identity()
        response = Usuarios.query. filter_by(id=id_usuario).first()
        if checkpw(senhaAtual, response.senha.encode('utf-8')):
            if verificaSenha(senha.decode('utf-8')):
                salt = gensalt()
                senha = hashpw(senha, salt).decode('utf-8')
                update = update(Usuarios).where(Usuarios.id == id_usuario).values(senha=senha)
                db.execute(update)
                db.commit()
                return jsonify({'status': 'success', 'msg': 'Senha atualizada com sucesso'})
            else:
                return jsonify({'status': 'senhaFraca'})
        else:
            return jsonify({'status': 'fail', 'msg': 'Senha incorreta'})        
    except Exception as e:
        print(e)
        
        
def inserirUsuario():
    try:
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        response = Usuarios.query.filter_by(email=email).first()
        if response:
            return jsonify({'status': 'fail', 'msg': 'Email já cadastrado'})
        else:
            if verificaSenha(senha):
                senha = senha.encode('utf-8')
                salt = gensalt()
                senha = hashpw(senha, salt).decode('utf-8')
                return redirect(url_for('mail_routes.enviarEmail', nome=nome, email=email, senha=senha))
            else:
                return jsonify({'status': 'senhaFraca'})
    except Exception as e:
        print(e)
    
            
        
