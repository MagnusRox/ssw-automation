import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def init_driver(request, browser):
    if browser == 'chrome':
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        web_driver = web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.cls.driver = web_driver
    yield
    web_driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption("--browser")