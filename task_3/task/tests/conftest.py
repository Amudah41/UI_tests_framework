import pytest
from task_3.framework.utils.Browser import Browser
from task_3.task.tests.test_data import URL


@pytest.fixture(scope="class")
def browser():
    browser = Browser()
    browser.get(URL)
    yield browser
    browser.quit()
