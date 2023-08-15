from app.__init__ import app

from sqlalchemy.sql import func
from sqlalchemy import create_engine, Column, Integer, VARCHAR, ForeignKey, Text, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Session
from werkzeug.security import check_password_hash, generate_password_hash
from app.helper import get_valid_filename, valid_password, valid_username
import time
from PIL import Image
from os.path import join


from os import environ
import dns.resolver

while True:
    try:
        db_ip = dns.resolver.query("database", "A")[0]
        break
    except dns.resolver.LifetimeTimeout:
        time.sleep(1)
        continue

ENGINE = create_engine(f"mysql://root:root@{db_ip}:3306/py_db", pool_pre_ping=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", VARCHAR(28), nullable=False)
    hash = Column("hash", Text, nullable=False)
    filename = Column("filename", VARCHAR(30), nullable=False, default="default.jpg")

    @staticmethod
    def create(username, password, filename) -> bool:
        """
            create user enitiy and
            return true if was created false otherwise
            can't return user entity because the instance in detached status
        """
        with Session(ENGINE) as sess:
            for user in sess.execute(select(User).where(User.username == username)).scalars():
                if check_password_hash(user.hash, password):
                    sess.close()
                    return None
            user = User(username=username, hash=generate_password_hash(password), filename=filename)
            sess.add(user)
            # add filename to user entity
            if filename:
                if (filename := get_valid_filename(filename, user.id)):
                    filename = Image.open(filename)
                    filename.thumbnail(app.config["PROFILE_IMAGES_DIMENSIONS"])
                    filename.save(join(app.config["PROFILE_IMAGES"], filename))
                    user.filename = filename
            sess.commit()
            return True

    @staticmethod
    def get(username, password) -> "User":
        if valid_username(username) and valid_password(password):
            sess = Session(ENGINE)
            sess.expire_on_commit = False
            stmt = select(User).where(User.username == username)
            for user in sess.execute(stmt).scalars():
                if check_password_hash(user.hash, password):
                    return {"user": user, "session": Session}
            return None

class Message(Base):
    __tablename__ = "messages"

    id = Column("id", Integer, primary_key=True)
    from_ = Column("from_room", Integer, ForeignKey("users.id"), nullable=False)
    to = Column("to_room", Integer, ForeignKey("users.id"), nullable=False)
    value = Column("value", Text, nullable=False)
    date = Column("date", DateTime, server_default=func.now())

    @staticmethod
    def create(from_, to, value) -> bool:
        with Session(ENGINE) as sess:
            message = Message(from_=from_, to=to, value=value)
            sess.add(message)
            sess.commit()
            return True

    @staticmethod
    def get():
        with Session(ENGINE) as sess:
            return sess.execute(select(Message).order_by(Message.date)).scalars()


# Base.metadata.drop_all(ENGINE)
Base.metadata.create_all(ENGINE)