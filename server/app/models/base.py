from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer


class Base(DeclarativeBase):
    pass


class IDMixin(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)