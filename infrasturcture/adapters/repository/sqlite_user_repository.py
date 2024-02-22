import sqlite3
from ...domain.models.user import User
from ...domain.ports.user_repository_port import UserRepositoryPort
from ...infrastructure.config.settings import SQLITE_DB_PATH

class SQLiteUserRepository(UserRepositoryPort):
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE_DB_PATH)
        self.cur = self.conn.cursor()

    def add_user(self, user: User) -> User:
        sql = ''' INSERT INTO users(name,last_name,cellphone,email,password,activation_token,verified_at)
                  VALUES(?,?,?,?,?,?,?) '''
        user_data = (user.name, user.last_name, user.cellphone, user.email, user.password, user.activation_token, user.verified_at)
        self.cur.execute(sql, user_data)
        self.conn.commit()
        return user

    def find_user_by_activation_token(self, token: str) -> User:
        self.cur.execute("SELECT * FROM users WHERE activation_token = ?", (token,))
        row = self.cur.fetchone()
        if row:
            return User(
                id=row[0],
                name=row[1],
                last_name=row[2],
                cellphone=row[3],
                email=row[4],
                password=row[5],
                activation_token=row[6],
                verified_at=row[7]
            )
        return None

    def update_user(self, user: User) -> None:
        sql = ''' UPDATE users
                SET name = ? ,
                    last_name = ? ,
                    cellphone = ? ,
                    email = ? ,
                    password = ? ,
                    activation_token = ? ,
                    verified_at = ?
                WHERE id = ? '''
        user_data = (
            user.name,
            user.last_name,
            user.cellphone,
            user.email,
            user.password,
            user.activation_token,
            user.verified_at,
            user.id
        )
        self.cur.execute(sql, user_data)
        self.conn.commit()

