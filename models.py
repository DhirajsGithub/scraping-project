from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    Headline = Column(String)
    Link = Column(String)
    Author = Column(String)
    Date = Column(String)
