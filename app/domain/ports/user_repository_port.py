from typing import Protocol
from ..models.user import User

class UserRepositoryPort(Protocol):
    def add_user(self, user: User) -> User:
        pass

    def find_user_by_email(self, email: str) -> User:
        pass

    def find_user_by_activation_token(self, token: str) -> User:
        pass

    def update_user(self, user: User) -> None:
        pass
