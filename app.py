from flask import Flask, request, jsonify
from models.User import db, Usuarios
from flask_migrate import Migrate
from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app, db)
db.init_app(app)
app.register_blueprint(user_bp, url_prefix='/')


@app.route('/')
def main():
    return "A API não explodiu"


if __name__ == '__main__':
    app.run(debug=True)
