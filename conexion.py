from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///biblioteca.db", echo=False)

Session = sessionmaker(bind=engine, expire_on_commit=False)