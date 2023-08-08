import pytest
from pages.login import Login
from tests.base_test import BaseTest
import source.config as cfg


class TestLogin(BaseTest):
    def test_url_opened(self):
        self.login = Login(self.driver)
        self.login.enter_speechace_home()
