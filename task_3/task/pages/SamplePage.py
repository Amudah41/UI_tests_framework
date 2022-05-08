from task_3.framework.pages.BaseForm import BaseForm
from selenium.webdriver.common.by import By


class SamplePageLocators:
    LOCATOR_SAMPLE_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//h1[@id='sampleHeading']",
    )


class SamplePage(BaseForm):
    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            SamplePageLocators.LOCATOR_SAMPLE_PAGE_UNIQUE_ELEMENT,
        )
