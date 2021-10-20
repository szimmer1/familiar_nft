from pydantic import BaseModel
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode = True