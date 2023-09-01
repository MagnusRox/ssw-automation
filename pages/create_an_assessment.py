import sys
from pages.base import Base
import source.config as cfg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAnAssessment(Base):
    button_create_new_assessment_workspaces = "//button[contains(text(),'Create New Assessment')]"
    button_assessment_with_custom_question = "//p[contains(text(),'Assessment with custom questions')]"
    button_custom_assessment = "//p[contains(text(),'Assessment with custom questions')]"
    button_next = "//button[contains(text(),'Next')]"

    heading_create_assessment = "//h2[contains(text(),'Create assessment')]"
    selection_check_custom_assessment = "//button[@class='Permisson__main-btn Permisson__main-btn--active']//p[" \
                                        "contains(text(),'Assessment with custom questions')] "
    heading_select_avatar = "//h2[contains(text(),'Select an avatar')]"
    heading_avatar_james = "//h3[contains(text(),'James')]"
    selection_check_james_selected = "//div[@class='Avatar Avatar--selected']//h3[contains(text(),'James')]"

    checkbox_weight = "//input[@type='checkbox']"
    text_weights_percentage = "//span[contains(text(),'Weights (%)')]"
    input_write_question = "//div[@class='CustomAssessmentQuestions__question-content-container'][{}]//input[@class='CustomAssessmentQuestions__input']"
    input_write_question_focussed = "//input[@class='CustomAssessmentQuestions__input CustomAssessmentQuestions__input--focused']"
    input_weight_box_question = "//div[@class='CustomAssessmentQuestions__question-content-container'][{}]//input[" \
                                "@class='CustomAssessmentQuestions__input " \
                                "CustomAssessmentQuestions__question-weight-input']"
    text_question_one_type = "//span[contains(text(),'Open Ended')]"

    button_question_type = "//button[@class='QuestionDetailsHeader__current-type-btn']"
    button_read_aloud_pronunciation = "//button[contains(text(),'Read-aloud (Pronunciation)')]"
    button_read_aloud_fluency = "//button[contains(text(),'Read-aloud (Fluency)')]"

    label_title_to_read_aloud = "//span[contains(text(),'Text to be read-aloud*')]"
    textarea_text_to_read_aloud = "//textarea[@class='QuestionPrompt__textarea QuestionPrompt__textarea CustomAssessmentQuestions__input']"

    heading_permission_settings = "//h2[contains(text(),'Permission settings')]"
    heading_deny_permissions = "//h3[contains(text(),'Users who deny permissions will not be able to con')]"
    button_default_audio_only = "//button[@class='Permisson__main-btn Permisson__main-btn--active']//p[text()='Records microphone']"

    button_audio_only = "//p[contains(text(),'Audio Only')]"
    button_audio_and_video = "//p[contains(text(),'Audio & Video')]"

    image_assessment_image = "//input[@class='AssessmentDetails__input-image']"
    input_assessment_name = "//input[@placeholder='Students']"
    input_assessment_description = "//input[@placeholder='Type something...']"

    display_assessment_name = "//p[contains(text(),'{}')]".format(cfg.assessment_name)
    display_assessment_description = "//p[contains(text(),'{}')]".format(cfg.assessment_description)

    heading_default_rubric = "//h2[contains(text(),'Set default rubric')]"
    text_cefr = "//span[contains(text(),'CEFR')]"
    text_ielts = "//span[contains(text(),'IELTS')]"
    text_pte = "//span[contains(text(),'PTE')]"
    text_toefl = "//span[contains(text(),'TOEFL')]"
    text_toeic = "//span[contains(text(),'TOEIC')]"
    text_speechace = "//span[contains(text(),'Speechace')]"
    input_rubric_name = "//input[@placeholder ='Speechace']"

    heading_score_settings = "//h2[contains(text(),'Score settings')]"
    heading_number_of_allowed_attempts = "//h4[contains(text(),'Number of allowed attempts')]"
    heading_evaluate_relevance_of_answer = "//h4[contains(text(),'Evaluate relevance of answer')]"
    select_option_unlimited_attempts = "//option[contains(text(),'Unlimited (Recommended)')]"
    heading_display_scores_to_taker = "//h4[contains(text(),'Displaying scores to test taker')]"
    checkbox_show_detailed_report_checked = "//span[text()='Show score summary and detailed report to candidate']/preceding-sibling::input[@checked]"

    button_submit = "//button[contains(text(),'Submit')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 30)

    def click_create_new_assessment(self):
        self._click(self.button_create_new_assessment_workspaces)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.heading_create_assessment)))

    def click_custom_assessment(self):
        self._click(self.button_assessment_with_custom_question)
        assert self.driver.find_element(By.XPATH, self.selection_check_custom_assessment) is not None
        self._click(self.button_next)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.heading_select_avatar)))

    def click_select_avatar(self):
        self._click(self.heading_avatar_james)
        assert self.driver.find_element(By.XPATH, self.selection_check_james_selected) is not None
        self._click(self.button_next)

    def click_weight_checkbox(self):
        self._click(self.checkbox_weight)
        assert self.driver.find_element(By.XPATH, self.text_weights_percentage) is not None

    def enter_question_one(self):
        self.driver.find_element(By.XPATH,self.input_write_question.format(1)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_write_question_focussed)))
        self.send_keys(self.input_write_question_focussed, cfg.custom_assessment_open_ended_question)
        assert self.driver.find_element(By.XPATH, self.text_question_one_type) is not None

    def enter_weights_one(self):
        self.send_keys(self.input_weight_box_question.format("1"), "50")

    def enter_question_two(self):
        self.driver.find_element(By.XPATH,self.input_write_question.format(2)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_write_question_focussed)))
        self.send_keys(self.input_write_question_focussed, cfg.custom_assessment_pronunciation_question)

    def enter_weights_two(self):
        self.send_keys(self.input_weight_box_question.format("2"), "25")
    def change_question_two_type(self):
        self._click(self.button_question_type)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_read_aloud_pronunciation)))
        self._click(self.button_read_aloud_pronunciation)
        assert self.driver.find_element(By.XPATH, self.label_title_to_read_aloud) is not None

    def question_two_enter_text_to_read_aloud(self):
        self.send_keys(self.textarea_text_to_read_aloud, cfg.custom_assessment_pronunciation_text)

    def enter_question_three(self):
        self.driver.find_element(By.XPATH,self.input_write_question.format(3)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_write_question_focussed)))
        self.send_keys(self.input_write_question_focussed, cfg.custom_assessment_fluency_question)
    def enter_weights_three(self):
        self.send_keys(self.input_weight_box_question.format("3"), "25")
    def change_question_three_type(self):
        self._click(self.button_question_type)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_read_aloud_fluency)))
        self._click(self.button_read_aloud_fluency)
        assert self.driver.find_element(By.XPATH, self.label_title_to_read_aloud) is not None

    def question_three_enter_text_to_read_aloud(self):
        self.send_keys(self.textarea_text_to_read_aloud, cfg.custom_assessment_fluency_text)
        self._click(self.button_next)

    def assert_persmission_settings(self):
        assert self.driver.find_element(By.XPATH, self.heading_permission_settings) is not None
        assert self.driver.find_element(By.XPATH, self.heading_deny_permissions) is not None
        assert self.driver.find_element(By.XPATH, self.button_default_audio_only) is not None

    def click_audio_only_assessment(self):
        self._click(self.button_audio_only)
        self._click(self.button_next)

    def click_audio_video_assessment(self):
        self._click(self.button_audio_and_video)
        self._click(self.button_next)

    def add_assessment_image(self):
        print(sys.path[1] + "/source/speechace_logo.png")
        self.send_keys(self.image_assessment_image, cfg.parent_dir + "/source/speechace_logo.png")

    def enter_assessment_name_and_description(self):
        self.send_keys(self.input_assessment_name, cfg.assessment_name)
        self.send_keys(self.input_assessment_description, cfg.assessment_description)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.display_assessment_name)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.display_assessment_description)))
        self._click(self.button_next)

    def assert_default_rubric(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.heading_default_rubric)))
        assert self.driver.find_element(By.XPATH, self.text_pte) is not None
        assert self.driver.find_element(By.XPATH, self.text_cefr) is not None
        assert self.driver.find_element(By.XPATH, self.text_ielts) is not None
        assert self.driver.find_element(By.XPATH, self.text_toefl) is not None
        assert self.driver.find_element(By.XPATH, self.text_toeic) is not None
        assert self.driver.find_element(By.XPATH, self.text_speechace) is not None
        assert self.driver.find_element(By.XPATH, self.input_rubric_name) is not None
        self._click(self.button_next)

    def assert_score_settings(self):
        assert self.driver.find_element(By.XPATH, self.heading_score_settings) is not None
        assert self.driver.find_element(By.XPATH, self.heading_number_of_allowed_attempts) is not None
        assert self.driver.find_element(By.XPATH, self.select_option_unlimited_attempts) is not None
        assert self.driver.find_element(By.XPATH, self.heading_evaluate_relevance_of_answer) is not None
        assert self.driver.find_element(By.XPATH, self.heading_display_scores_to_taker) is not None
        assert self.driver.find_element(By.XPATH, self.checkbox_show_detailed_report_checked) is not None

    def click_submit_button(self):
        self._click(self.button_submit)
