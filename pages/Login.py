import time

from pages.base import Base
import source.config as cfg
class Login(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def enter_speechace_home(self):
        self.driver.get(cfg.test_url)
        time.sleep(5)
