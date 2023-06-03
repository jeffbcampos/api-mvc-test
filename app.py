from flask import Flask
from flask_migrate import Migrate
from routes.bluePrints import blue_prints
from control.MainController import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app, db)
db.init_app(app)
CORS(app)
jwt = JWTManager(app)
for bp in blue_prints:
    app.register_blueprint(bp)

@app.route('/')
def main():
    return "A API não explodiu"


if __name__ == '__main__':
    app.run(debug=True)
