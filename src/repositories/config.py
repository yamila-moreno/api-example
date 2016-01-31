from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings.base import config

metadata = MetaData()
Base = declarative_base(metadata=metadata)
engine = create_engine(URL(**config['database']))
DBSession = sessionmaker(bind=engine)
