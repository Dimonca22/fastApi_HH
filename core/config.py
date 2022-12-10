from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("FH_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("FA_SECRET_KEY", cast=str, default='5a72859e704fb2be9c76542ca3e888854244e727c84c9277fab42429e7d5c9d6')
