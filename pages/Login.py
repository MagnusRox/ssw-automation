import time

from pages.base import Base
import source.config as cfg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(Base):
    title_speech_xpath = "//span[contains(text(),'speech')]"
    modal_title_login = "//h2[contains(text(),'Log in')]"

    # buttons
    button_login_xpath = "//button[contains(text(),'Log in')]"
    modal_button_create_an_account = "//button[contains(text(),'Create an account')]"
    modal_button_sign_in = "//button[contains(text(),'Sign in')]"
    modal_button_forgot_password = "//button[contains(text(),'Forgot Password?')]"

    # modal
    modal_entire_model_login = "//body/div[@id='react-app']/div[1]/div[2]"

    # inputs
    modal_input_username = '//input[@name = "username"]'
    modal_input_password = '//input[@name = "password"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def enter_speechace_home(self):
        self.driver.get(cfg.test_url)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.title_speech_xpath)))

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        self._click(self.button_login_xpath)

    def assert_login_modal(self):
        assert self.driver.find_element(By.XPATH, self.modal_entire_model_login) is not None
        assert self.driver.find_element(By.XPATH, self.modal_button_create_an_account) is not None
        assert self.driver.find_element(By.XPATH, self.modal_button_forgot_password) is not None

        assert self.driver.find_element(By.XPATH, self.modal_button_sign_in) is not None
        assert self.driver.find_element(By.XPATH, self.modal_input_username) is not None
        assert self.driver.find_element(By.XPATH, self.modal_input_password) is not None

        assert self.driver.find_element(By.XPATH, self.modal_title_login) is not None

    def enter_username(self):
        self.send_keys(self.modal_input_username, cfg.admin_username)
        time.sleep(0.5)

    def enter_password(self):
        self.send_keys(self.modal_input_password, cfg.admin_password)
        time.sleep(0.5)

    def click_sign_in(self):
        self._click(self.modal_button_sign_in)
