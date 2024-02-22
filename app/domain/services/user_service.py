from datetime import datetime
import bcrypt
from ..models.user import User
from ..ports.user_repository_port import UserRepositoryPort
from ..ports.email_service_port import EmailServicePort
import secrets

class UserService:
    def __init__(self, user_repository: UserRepositoryPort, email_service: EmailServicePort):
        self.user_repository = user_repository
        self.email_service = email_service

    def register_user(self, user_data: dict) -> User:
        user_data['password'] = self.encrypt_password(user_data['password'])
        user_data['activation_token'] = self.generate_activation_token()
        user = self.user_repository.add_user(User(**user_data))
        self.send_activation_email(user)
        return user

    def encrypt_password(self, plain_password: str) -> str:
        return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def generate_activation_token(self) -> str:
        return secrets.token_urlsafe(16)  

    def send_activation_email(self, user: User):
        activation_link = f"https://yourdomain.com/api/v1/users/{user.activation_token}/activate"
        email_body = f"Please click on the link to activate your account: {activation_link}"
        self.email_service.send_email(user.email, "Activate your account", email_body)