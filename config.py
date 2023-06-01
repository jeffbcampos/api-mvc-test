import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv("LINK_PG")
