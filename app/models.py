from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    recipes = relationship(
        "Recipe",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )


class Recipe(Base):
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=True)
    url = Column(String(256), index=True, nullable=True)
    source = Column(String(256), nullable=True)
    submitter_id = Column(String(10), ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="recipes")
