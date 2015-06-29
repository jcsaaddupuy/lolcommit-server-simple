# coding: utf-8

from flaskext.uploads import IMAGES

class Config(object):
    DEBUG = False
    TESTING = False
    UPLOADED_FILES_ALLOW=IMAGES
    UPLOADS_DEFAULT_DEST='/tmp/lolcommits'

