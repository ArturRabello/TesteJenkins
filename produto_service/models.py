from sqlalchemy import Column, Integer, String, Float
from database import Base


class Produto(Base):
    __tablename__ = "produto"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    preco = Column(Float)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "preco": self.preco
        }
    
    