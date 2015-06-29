# coding: utf-8
from __future__ import unicode_literals
from lolcommitss import appfactory


DEFAULT_CONFIG_OBJ='lolcommitss.settings.defaults'
# uncomment this to for using an envvar
# DEFAULT_CONFIG_ENVVAR="LOLCOMMITSS_SETTINGS"

def make_app():
    app = appfactory.create_app(__name__)
    appfactory.configure_all(app, from_default_obj=DEFAULT_CONFIG_OBJ)
    # uncomment this to for using an envvar, and remove the line above
    #appfactory.configure_all(app, from_default_obj=DEFAULT_CONFIG_OBJ, from_envvar=DEFAULT_CONFIG_ENVVAR)
    appfactory.register_all(app)
    return app

app = make_app()
