import pytest
from task_2.config.webdriver import WebDriver


@pytest.fixture(scope="function")
def browser():
    browser = WebDriver().driver
    yield browser
    browser.quit()
