# coding: utf-8
import unittest
from tests.base  import BaseTestCase


class DefaultViewTestCase(BaseTestCase):
    """ Unitests for client view """

    def test_get_root(self):
        res = self.client.get('/')
        assert res.status_code == 200
        assert "Hello world" in res.data

    def test_get_root_with_name(self):
        res = self.client.get('/?name=jOhn')
        assert res.status_code == 200
        assert "Hello John" in res.data


if __name__ == '__main__':
    unittest.main()
