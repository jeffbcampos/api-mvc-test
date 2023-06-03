from flask import Flask
from flask_migrate import Migrate
from routes.users_routes import users_routes
from routes.filmes_routes import filmes_routes
from routes.series_routes import series_routes
from control.MainController import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app, db)
db.init_app(app)
app.register_blueprint(users_routes, url_prefix='/')
app.register_blueprint(filmes_routes, url_prefix='/')
app.register_blueprint(series_routes, url_prefix='/')
CORS(app)
jwt = JWTManager(app)

@app.route('/')
def main():
    return "A API não explodiu"


if __name__ == '__main__':
    app.run(debug=True)
