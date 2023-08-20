from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class Base:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def _click(self,element_xpath):
        element = WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH, element_xpath)))
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self,element_xpath, value):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, element_xpath)))
        self.driver.execute_script("arguments[0].click();", element)
        element.send_keys(value)
