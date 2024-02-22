import jwt
from datetime import datetime, timedelta
from ...infrastructure.config.settings import JWT_SECRET

class JWTAdapter:
    @staticmethod
    def generate_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def verify_token(token: str) -> dict:
        decoded_jwt = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded_jwt
