from hashlib import sha256
from peewee import CharField, Model, SqliteDatabase

db = SqliteDatabase("kivy_app.db")


class User(Model):
    email = CharField()
    username = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


def password_hasher(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def create_user(email: str, username: str, password: str) -> User:
    return User.create(
        email=email, username=username, password=password_hasher(password)
    )


def authenticate_user(username: str, password: str) -> bool:
    try:
        user = User.get(User.username == username)
        return user.password == password_hasher(password)
    except User.DoesNotExist:
        return False


def get_user(username: str) -> User:
    try:
        return User.get(User.username == username)
    except User.DoesNotExist:
        return None


with db:
    db.create_tables([User])
