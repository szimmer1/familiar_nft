from sqlalchemy import Column, String
from models import Base, OrmBaseModel


class User(Base):
    __tablename__ = "users"
    account_id = Column(String(255), primary_key=True)
    nonce = Column(String(63), nullable=False, index=False, unique=False)
