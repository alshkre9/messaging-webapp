from sqlalchemy.sql import func
from sqlalchemy import create_engine, Column, Integer, VARCHAR, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import DeclarativeBase

from os import environ
import enum

password = environ.get('mysql_password')
ENGINE = create_engine(f"mysql://root:{password}@localhost:3306/website")

class Room_type(enum.Enum):
    group = "Group"
    friendship = "Friendship"

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column("username", VARCHAR(28), nullable=False)
    hash = Column("hash", Text, nullable=False)
    filename = Column("filename", VARCHAR(30), nullable=False, default="default.jpg")

class Room(Base):
    __tablename__ = "rooms"

    id = Column("id", Integer, primary_key=True)
    model = Column("model", VARCHAR(12), Enum(Room_type), nullable=False) 

class Group(Base):
    __tablename__ = "groups"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", VARCHAR(28), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column("room_id", Integer, ForeignKey("rooms.id"), nullable=False)

class Friendship(Base):
    __tablename__ = "friendships"

    id = Column("id", Integer, primary_key=True)
    user_id1 = Column("user_id1", Integer, ForeignKey("users.id"), nullable=False)
    user_id2 = Column("user_id2", Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column("room_id", Integer, ForeignKey("rooms.id"), nullable=False)

class Friendshiprequest(Base):
    __tablename__ = "requests"

    id = Column("id", Integer, primary_key=True)
    sender_id = Column("sender_id", Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column("receiver_id", Integer, ForeignKey("users.id"), nullable=False)

class Message(Base):
    __tablename__ = "messages"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column("room_id", Integer, ForeignKey("rooms.id"), nullable=False)
    value = Column("value", Text, nullable=False)
    date = Column("date", DateTime, server_default=func.now())

# Base.metadata.drop_all(ENGINE)
Base.metadata.create_all(ENGINE)