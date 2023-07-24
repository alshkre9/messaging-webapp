from sqlalchemy.sql import func
from sqlalchemy import create_engine, Column, Integer, VARCHAR, ForeignKey, Text, DateTime
from sqlalchemy.orm import DeclarativeBase

from os import environ

# password = environ.get('mysql_password')
import dns.resolver
ENGINE = create_engine(f"mysql://root:root@:3306/website", pool_pre_ping=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", VARCHAR(28), nullable=False)
    hash = Column("hash", Text, nullable=False)
    filename = Column("filename", VARCHAR(30), nullable=False, default="default.jpg")

class Friendship(Base):
    __tablename__ = "friendships"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    friend_id = Column("friend_id", Integer, ForeignKey("users.id"), nullable=False)

class Message(Base):
    __tablename__ = "messages"

    id = Column("id", Integer, primary_key=True)
    from_ = Column("from_room", Integer, ForeignKey("users.id"), nullable=False)
    to = Column("to_room", Integer, ForeignKey("users.id"), nullable=False)
    value = Column("value", Text, nullable=False)
    date = Column("date", DateTime, server_default=func.now())

class Friendshiprequest(Base):
    __tablename__ = "requests"

    id = Column("id", Integer, primary_key=True)
    sender_id = Column("sender_id", Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column("receiver_id", Integer, ForeignKey("users.id"), nullable=False)

# class Group(Base):
#     __tablename__ = "groups"

# Base.metadata.drop_all(ENGINE)
Base.metadata.create_all(ENGINE)