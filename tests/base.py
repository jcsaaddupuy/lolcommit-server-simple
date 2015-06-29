import os
import unittest
import tempfile
from  lolcommitss import appfactory

from lolcommitss.models import Base



# find abs path to this script
root_dir = os.path.abspath(os.path.dirname(__file__))
ENV_VAR_NAME="LOLCOMMITSS_SETTINGS"

SETTINGS_TESTS_CFG=os.path.join(
        root_dir,
        '..',
        'lolcommitss',
        'settings',
        'tests.cfg'
)

DEFAULT_CONFIG_OBJ='lolcommitss.settings.defaults'


class BaseTestCase(unittest.TestCase):
    TMP_DB = os.path.join(tempfile.gettempdir(), "lolcommitss-tmp.db")

    def setUp(self):
        # remove tmp db if exists
        if os.path.exists(self.TMP_DB):
            os.unlink(self.TMP_DB)

        # app configuration
        config_obj = 'lolcommitss.settings.defaults'
        os.environ[ENV_VAR_NAME]=SETTINGS_TESTS_CFG

        app = appfactory.create_app(__name__)
        appfactory.configure_app(app, from_default_obj=config_obj, from_envvar=ENV_VAR_NAME)
        appfactory.register_all(app)

        self.app = app
        self.client = app.test_client()


if __name__ == '__main__':
    unittest.main()
