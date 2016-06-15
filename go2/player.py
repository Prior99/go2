from sqlalchemy import Column, Integer, String
from go2.database import Base

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
