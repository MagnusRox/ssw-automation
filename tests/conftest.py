import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.quit()



