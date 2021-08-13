import os

from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, Date, ForeignKey, Time, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

full_path = os.path.join(os.path.realpath(".."), r"psychology\db.sqlite3")
print(full_path)
engine = create_engine(f"sqlite:///{full_path}")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)

class Meetings(Base):
    __tablename__ = "main_app_meetings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("auth_user.id"))
    description = Column(Text(255))
    phone_number = Column(String)
    is_accepted = Column(Boolean)
    time_start = Column(Time)
    time_end = Column(Time)
    date = Column(Date)
    is_done = Column(Boolean)


class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True)
    password = Column(String(128))
    last_login = Column(DateTime)
    is_superuser = Column(Boolean)
    username = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(254))
    is_staff = Column(Boolean)
    is_active = Column(Boolean)
    date_joined = Column(DateTime)
    first_name = Column(String(150))
