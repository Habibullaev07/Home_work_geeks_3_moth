from sqlalchemy import DateTime, CheckConstraint, Integer, String, Float, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(30), nullable=False)
    balance: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=True, default=0)
    deposit_balance: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=True,
                                                   default=50000)

    
    __table_args__ = (CheckConstraint('balance >= 0', name='balance_cannot_be_less_than_zero'),
                      CheckConstraint('deposit_balance >= 0',
                                      name='dep_balance_cannot_be_less_than_zero'))

class Text_for_handlers(Base):
    __tablename__ = 'text_for_handlers'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
