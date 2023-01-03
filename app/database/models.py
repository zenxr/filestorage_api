import sqlalchemy
from database import base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext import declarative


class _BaseMixin:
    id: sqlalchemy.Integer
    __name__: str

    # requires in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an exipired load
    __mapper_args__ = {"eager_defaults": True}

    @declarative.declared_attr
    def __tablename__(cls) -> str:
        # Generate __tablename__ automatically
        return cls.__name__.lower()


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
