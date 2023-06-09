from flask import Blueprint
from control.MailController import enviarEmail, confirmarEmail

mail_routes = Blueprint('mail_routes', __name__)

mail_routes.route('/enviarEmail', methods=['GET'])(enviarEmail)
mail_routes.route('/confirmarEmail/<token>', methods=['GET'])(confirmarEmail)