from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

Base = declarative_base()

import server.database.game
import server.database.player

engine = create_engine(config.database_uri, echo=True)

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=True)
session = DBSession()
