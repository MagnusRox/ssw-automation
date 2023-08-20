import pytest
from pages.login import Login
from tests.base_test import BaseTest
import time


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.login = Login(self.driver)

    def test_open_url(self):
        self.login.enter_speechace_home()

    def test_click_login_and_evaluate_modal(self):
        self.login.click_login()
        self.login.assert_login_modal()

    def test_enter_credentials(self):
        self.login.enter_username()
        self.login.enter_password()
        self.login.click_sign_in()
        time.sleep(10)
