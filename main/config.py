import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
ACCESS_TOKEN_KEY = os.environ.get("ACCESS_TOKEN_KEY") or "access_token"
REFRESH_TOKEN_KEY = os.environ.get("REFRESH_TOKEN_KEY") or "refresh_token"
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATION = False
ACCESS_TOKEN_LIFE_TIME = 86400
REFRESH_TOKEN_LIFE_TIME = 86400 * 30
ALGORITHM = "HS256"
