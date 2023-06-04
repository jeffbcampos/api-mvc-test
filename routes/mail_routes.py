from flask import Blueprint
from control.MailController import enviarEmail

mail_routes = Blueprint('mail_routes', __name__)

mail_routes.route('/enviarEmail', methods=['GET'])(enviarEmail)