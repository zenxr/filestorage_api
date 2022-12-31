import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm

import conf

engine = sqlalchemy.create_engine(conf.AppConfig.from_env().database_uri)

_SessionFactory = orm.sessionmaker(bind=engine)

Base = declarative_base()

def session_factory() -> orm.Session:
    Base.metadata.create_all(engine)
    return _SessionFactory()
