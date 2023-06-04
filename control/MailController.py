from flask import redirect, url_for, request, jsonify
from control.MainController import db
from datetime import timedelta
from models.Verificacao import Verificacao
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token

apiUrl = 'http://localhost:5000'

def enviarEmail():
    from app import mail
    from flask_mail import Message
    
    try:
        email = request.args.get('email')
        senha = request.args.get('senha')
        nome = request.args.get('nome')
        tokenEmail = create_access_token(identity=email, expires_delta=timedelta(minutes=30))
        novo_user = Verificacao(nome=nome, email=email, senha=senha, token=tokenEmail)
        db.session.add(novo_user)
        db.session.commit()
        msg = Message('Confirmação de email', sender='project-rec@outlook.com', recipients=[f'{email}'])
        url = f'{apiUrl}/confirmarEmail/{tokenEmail}'
        msg.html = f'''        
            <p>Confirme seu cadastro através do link abaixo:</p>
            <a href="{url}">
                {url}
            </a>'''
        mail.send(msg)
        return jsonify({'status': 'success', 'msg': 'Email enviado com sucesso'})
    except Exception as e:
        print(e)