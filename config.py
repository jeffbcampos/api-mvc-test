import os
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv("LINK_PG")
JWT_SECRET_KEY = os.getenv("JWT_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=5)
