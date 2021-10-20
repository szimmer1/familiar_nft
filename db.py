from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://localhost:5432", echo=True)

Session = sessionmaker(autocommit=True, autoflush=False, bind=engine)

