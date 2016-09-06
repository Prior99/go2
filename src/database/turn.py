from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.database import Base

class PrisonerCount(Base):
    __tablename__ = 'prisoner_count'
    id = Column(Integer, primary_key=True)
    player = relationship('Player')
    count = Columnt(Integer, nullable=False)

class Turn(Base):
    __tablename__ = 'turn'
    id = Column(Integer, primary_key=True)
    board = Column(String(128), nullable=False)
    turn_number = Column(Integer, nullable=False)
    prisoners = relationship('PrisonerCount')
