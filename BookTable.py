from sqlalchemy import Column, Integer, String
from .DBConnection import Base

class BookTable(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    genre = Column(String(255), nullable=False)

    def __repr__(self):
        return f"Book(id='{self.id}', email='{self.title}', password='{self.genre}')"
