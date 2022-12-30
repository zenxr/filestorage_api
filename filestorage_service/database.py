from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
import functools

import conf
from databases import Database as _Database

engine = create_engine(conf.AppConfig.from_env().database_uri)
metadata = MetaData()

# TODO
# - add timestamp metadata (creation, update, etc)
# - add user
# - add api key

bucket = Table(
    "bucket",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String(100)),
    Column("name", String(50)),
)

file = Table(
    "file",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("path", String(50)),
    Column("bucket", String(100)),
)


@functools.lru_cache
def get():
    return _Database(conf.AppConfig.from_env().database_uri)
