from sqlalchemy import Integer, String, DateTime, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Register(Base):

    __tablename__ = 'register'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_tg: Mapped[int] = mapped_column(Integer, nullable=False)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    
    
class Task(Base):
    __tablename__ = 'task'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_tg: Mapped[int] = mapped_column(Integer, nullable=False)
    name_task : Mapped[str]  = mapped_column(String(30), nullable=True)
    description: Mapped[str]  = mapped_column(Text)
    

class LongWords(Base):
    __tablename__ = 'long_words'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    

    