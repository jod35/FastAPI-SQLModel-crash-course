from sqlmodel import SQLModel
from models import Book
from database import engine

print("CREATING DATABASE.....")

SQLModel.metadata.create_all(engine)