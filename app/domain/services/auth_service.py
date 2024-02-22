import jwt
from datetime import datetime, timedelta
from ..models.user import User
from ..ports.user_repository_port import UserRepositoryPort

class AuthService:
    def __init__(self, user_repository: UserRepositoryPort, jwt_secret: str):
        self.user_repository = user_repository
        self.jwt_secret = jwt_secret

    def generate_jwt(self, user: User) -> str:
        payload = {
            "user_id": user.id,  
            "exp": datetime.utcnow() + timedelta(days=1)
        }
        return jwt.encode(payload, self.jwt_secret, algorithm="HS256")

    def verify_jwt(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.jwt_secret, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
