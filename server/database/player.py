from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from server.database import Base

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    secret = Column(String(130), nullable=False)
    games = relationship('Game', 
        secondary='assoc_player_game',
        back_populates='players')
