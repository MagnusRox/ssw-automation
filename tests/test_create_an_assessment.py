from tests.base_test import BaseTest
import pytest

from pages.login import Login
from pages.create_a_workspace import CreateAWorkspace
from pages.create_an_assessment import CreateAnAssessment


@pytest.mark.createanassessment
class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.login = Login(self.driver)
        self.create_workspace = CreateAWorkspace(self.driver)
        self.create_assessment = CreateAnAssessment(self.driver)

    def test_login(self):
        self.login.enter_speechace_home()
        self.login.click_login()
        self.login.enter_username()
        self.login.enter_password()
        self.login.click_sign_in()

    def test_open_workspace_home(self):
        self.create_workspace.click_open_workspaces()

    def test_click_create_new_assessment(self):
        self.create_assessment.click_create_new_assessment()

    def test_click_custom_assessment(self):
        self.create_assessment.click_custom_assessment()

    def test_select_avatar(self):
        self.create_assessment.click_select_avatar()

    def test_enter_questions(self):
        self.create_assessment.click_weight_checkbox()
        self.create_assessment.enter_question_one()
        self.create_assessment.enter_weights_one()
        self.create_assessment.enter_question_two()
        self.create_assessment.change_question_two_type()
        self.create_assessment.enter_weights_two()
        self.create_assessment.question_two_enter_text_to_read_aloud()
        self.create_assessment.enter_question_three()
        self.create_assessment.enter_weights_three()
        self.create_assessment.change_question_three_type()
        self.create_assessment.question_three_enter_text_to_read_aloud()
        self.create_assessment.assert_persmission_settings()

    def test_assessment_permissions(self):
        self.create_assessment.click_audio_only_assessment()

    def test_add_assessment_details(self):
        self.create_assessment.add_assessment_image()
        self.create_assessment.enter_assessment_name_and_description()

    def test_rubric(self):
        self.create_assessment.assert_default_rubric()

    def test_score_Settings(self):
        self.create_assessment.assert_score_settings()

    def test_create_assessment(self):
        self.create_assessment.click_submit_button()






