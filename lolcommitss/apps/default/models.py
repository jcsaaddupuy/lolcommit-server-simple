# coding: utf-8
from sqlalchemy import Column, Integer, String
from lolcommitss.models import Base

from flask import current_app as c



class LolCommit(Base):
    __tablename__ = 'lolcommit'

    id = Column(Integer, primary_key=True)

    repo = Column(String)
    filename = Column(String)
    message = Column(String)
    author_name = Column(String)
    author_email = Column(String)
    sha = Column(String)



    def photo_url(self):
        return c.photos.url(self.filename)
