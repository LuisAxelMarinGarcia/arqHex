from pymongo import MongoClient
from ...domain.models.user import User
from ...domain.ports.user_repository_port import UserRepositoryPort
from ...infrastructure.config.settings import DATABASE_URL

class MongoUserRepository(UserRepositoryPort):
    def __init__(self):
        self.client = MongoClient(DATABASE_URL)
        self.db = self.client.mydatabase
        self.collection = self.db.users

    def add_user(self, user: User) -> User:
        result = self.collection.insert_one(user.dict())
        user.id = result.inserted_id
        return user

    def find_user_by_email(self, email: str) -> User:
        user_data = self.collection.find_one({"email": email})
        if user_data:
            return User(**user_data)
        return None
    
    def find_user_by_activation_token(self, token: str) -> User:
        user_data = self.collection.find_one({"activation_token": token})
        if user_data:
            return User(**user_data)
        return None

    def update_user(self, user: User) -> None:
        self.collection.update_one(
            {"_id": user.id},
            {"$set": user.dict()}
        )


