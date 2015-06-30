# coding: utf-8
from sqlalchemy import Column, Integer, String
from lolcommitss.models import Base



class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    repo = Column(String)
    filename = Column(String)
