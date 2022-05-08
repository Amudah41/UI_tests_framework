import pytest
from task_2.pages.MainPage import MainPage
from task_2.pages.AboutPage import AboutPage
from task_2.config.config_data import TimeOut_default
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchLocators:
    LOCATOR_MAIN_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//div[contains(@id, 'home_maincap')]",
    )
    LOCATOR_ABOUT_PAGE_UNIQUE_ELEMENT = (By.XPATH, "//div[@id='about_header_area']")


class TestCase1:
    def test_case_1(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        assert self.is_page_open(browser, "main_page"), "Can't open the main page."

        main_page.click_on_the_about_page_button()
        assert self.is_page_open(browser, "about_page"), "Can't open the about page."

        about_page = AboutPage(browser)

        assert about_page.take_count_of_gamers(
            "in_game"
        ) < about_page.take_count_of_gamers(
            "online"
        ), "Count of gamers in game more than online."

        about_page.click_on_the_main_page_button()
        assert self.is_page_open(browser, "main_page"), "Can't open the main page."

    @staticmethod
    def is_page_open(browser, page):
        page_locators = {
            "main_page": SearchLocators.LOCATOR_MAIN_PAGE_UNIQUE_ELEMENT,
            "about_page": SearchLocators.LOCATOR_ABOUT_PAGE_UNIQUE_ELEMENT,
        }
        try:
            WebDriverWait(browser, TimeOut_default).until(
                EC.presence_of_element_located(page_locators[page])
            )
            return True
        except TimeoutException:
            return False
