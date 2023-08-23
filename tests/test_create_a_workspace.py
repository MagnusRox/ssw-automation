from tests.base_test import BaseTest
import pytest

from pages.login import Login
from pages.create_a_workspace import CreateAWorkspace


@pytest.mark.createaworkspace
class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.login = Login(self.driver)
        self.create_workspace = CreateAWorkspace(self.driver)


    def test_login(self):
        self.login.enter_speechace_home()
        self.login.click_login()
        self.login.enter_username()
        self.login.enter_password()
        self.login.click_sign_in()

    def test_open_workspace_home(self):
        self.create_workspace.click_open_workspaces()

    def test_create_new_workspace(self):
        self.create_workspace.click_more_options()
        self.create_workspace.click_create_new_workspace()

    def test_upload_workspace_image(self):
        self.create_workspace.upload_workspace_image_and_enter_details()

    def test_click_create_workspace(self):
        self.create_workspace.click_create_workspace()
        self.create_workspace.assertion_post_workspace_creations()


