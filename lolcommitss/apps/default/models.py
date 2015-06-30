# coding: utf-8
from sqlalchemy import Column, Integer, String
from lolcommitss.models import Base

from flask import current_app as c



class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    repo = Column(String)
    filename = Column(String)


    def url(self):
        return c.photos.url(self.filename)
