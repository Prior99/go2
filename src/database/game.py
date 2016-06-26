from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.database import Base

class PlayerGameAssoc(Base):
    __tablename__ = 'assoc_player_game',
    id = Column(Integer, primary_key=True)
    game = Column('game', Integer, ForeignKey('game.id'))
    player = Column('player', Integer, ForeignKey('player.id'))
    accepted = Column('accepted', Boolean)

class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)
    players = relationship('Player',
        secondary='assoc_player_game',
        back_populates='games')
