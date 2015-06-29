# coding: utf-8
from __future__ import unicode_literals

from flask import Flask
import logging


def create_app(name):
    app = Flask(name)
    return app


def configure_all(app, from_default_obj, from_envvar=None):
    configure_app(app, from_default_obj, from_envvar)
    configure_loggers(app)
    configure_uploads(app)

def configure_app(app, from_default_obj, from_envvar=None):
    app.config.from_object(from_default_obj)
    if from_envvar:
        app.config.from_envvar(from_envvar)

def configure_loggers(app):
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

def configure_uploads(app):
    from flaskext.uploads import UploadSet, IMAGES, configure_uploads as config_uploads
    app.photos = UploadSet('lolcommit', IMAGES)
    config_uploads(app, (app.photos,))


def register_all(app):
    register_blueprints(app)


def register_blueprints(app):
    from lolcommitss.apps.default import views as default_views
    # app.register_blueprint(default_views.blueprint, url_prefix='/')
    app.register_blueprint(default_views.blueprint)
