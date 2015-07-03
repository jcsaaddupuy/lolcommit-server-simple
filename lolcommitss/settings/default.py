# coding: utf-8

from flaskext.uploads import IMAGES

class Config(object):
    DEBUG = False
    TESTING = False

    # static folder inside app
    # STATIC_FOLDER = 'static'

    UPLOADED_FILES_ALLOW=IMAGES
    UPLOADS_DEFAULT_DEST='/data/uploads'
    SQLALCHEMY_DATABASE_URI="sqlite:////data/foo.db"

