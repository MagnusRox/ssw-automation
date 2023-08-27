import time
import sys
from pages.base import Base
import source.config as cfg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAWorkspace(Base):
    button_workspaces = "//button[contains(text(),'Workspaces')]"
    url_partial_workspaces = "https://yanpix.speechace.com/placement/workspaces"
    tree_item_my_assessments = "//span[contains(text(),'my assessments')]"

    more_workspace_options = "//button[contains(text(),'⋮')]"
    button_create_new_workspace = '//button[@class="Menu-list__item ControlDropdown__action-btn"]'
    title_create_workspace = "//h2[@class='CreateWorkspace__title']"
    heading_info_create_workspace = "//h3[contains(text(),'To begin, let’s create a Workspace.')]"

    button_upload_your_image = "//label[text()='Upload your logo']"
    input_image_url = "//input[@class='LogoStage__input']"
    input_workspace_name = '//input[@name="name"]'
    input_workspace_description = '//input[@name="description"]'
    button_create = "//button[contains(text(),'Create')]"

    # string matching for Asserts
    text_create_workspace_title = "Welcome, Automation_Admin!"
    placeholder_workspace_description = "Description (max length 40 symbols)"
    placeholder_workspace_name = "Name (max length 20 symbols)"

    heading_my_assessments = "//h1[contains(text(),'My Assessments')]"
    button_create_new_assessment = "//button[contains(text(),'Create New Assessment')]"
    text_created_workspace_name = "//p[contains(text(),'{}')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 30)

    def click_open_workspaces(self):
        self._click(self.button_workspaces)
        assert self.url_partial_workspaces in self.driver.current_url
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.tree_item_my_assessments)))

    def click_more_options(self):
        self._click(self.more_workspace_options)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_create_new_workspace)))

    def click_create_new_workspace(self):
        self._click(self.button_create_new_workspace)
        time.sleep(5)
        assert self.driver.current_url == cfg.url_create_workspace
        assert self.driver.find_element(By.XPATH, self.title_create_workspace) is not None
        assert self.driver.find_element(By.XPATH, self.title_create_workspace).text == self.text_create_workspace_title
        assert self.driver.find_element(By.XPATH, self.heading_info_create_workspace) is not None
        assert self.driver.find_element(By.XPATH, self.input_workspace_name).get_attribute(
            'placeholder') == self.placeholder_workspace_name
        assert self.driver.find_element(By.XPATH, self.input_workspace_description).get_attribute(
            'placeholder') == self.placeholder_workspace_description
        assert self.driver.find_element(By.XPATH, self.button_create) is not None
        assert self.driver.find_element(By.XPATH, self.button_create).is_enabled() == False

    def upload_workspace_image_and_enter_details(self):
        #self.driver.find_element(By.XPATH,self.button_upload_your_image).click()
        self.send_keys(self.input_image_url,sys.path[1] +"/source/speechace_logo.png")
        workspace_name = self.set_workspace_name()
        self.send_keys(self.input_workspace_name, workspace_name)
        cfg.current_workspace_name = workspace_name
        self.send_keys(self.input_workspace_description, " This is a test description ")

    def click_create_workspace(self):
        self._click(self.button_create)

    def assertion_post_workspace_creations(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.heading_my_assessments)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.button_create_new_assessment)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_created_workspace_name.format(cfg.current_workspace_name))))

    @staticmethod
    def set_workspace_name():
        current_workspace_name_split = cfg.current_workspace_name.split(" ")
        return current_workspace_name_split[0] + " " + str(int(current_workspace_name_split[1]) + 1)
