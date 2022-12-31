from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    ForeignKey,
    create_engine,
)
from sqlalchemy.ext import declarative
import functools

from database import base


class _BaseMixin(object):
    @declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() # type: ignore

    id = Column(Integer, primary_key=True)


class Bucket(base.Base, _BaseMixin):
    path = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)


class File(base.Base, _BaseMixin):
    path = Column(String(50), nullable=False)
    bucket_id = Column(Integer, ForeignKey("bucket.id"))


class User(base.Base, _BaseMixin):
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)


class ApiKey(base.Base, _BaseMixin):
    user = Column(Integer, ForeignKey("user.id"))
    key = Column(String(50), nullable=False)
