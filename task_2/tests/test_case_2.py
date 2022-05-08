import pytest
from task_2.pages.MainPage import MainPage
from task_2.pages.LeaderPage import LeaderPage
from task_2.pages.GamePage import GamePage
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
    LOCATOR_LEADER_PAGE_UNIQUE_ELEMENT = (By.XPATH, "//div[@id='search_results']")
    LOCATOR_GAME_PAGE_UNIQUE_ELEMENT = (By.XPATH, "//div[@id='game_highlights']")

    LOCATOR_LINUX_CHECKBOX = (
        By.XPATH,
        '//span[@data-value="linux" and contains(@class, "checked")]',
    )
    LOCATOR_LAN_CHECKBOX = (
        By.XPATH,
        '//span[@data-value="48" and contains(@class,"checked")]',
    )
    LOCATOR_ACTION_CHECKBOX = (
        By.XPATH,
        '//span[@data-value="19" and contains(@class,"checked")]',
    )


class TestCase2:
    def test_case_2(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        assert self.is_page_open(browser, "main_page"), "Can't open the main page."

        main_page.click_on_the_leader_page_button()
        assert self.is_page_open(browser, "leader_page"), "Can't open the leader page."

        leader_page = LeaderPage(browser)
        leader_page.click_on_the_linux_checkbox()
        assert self.is_checked(
            browser, "linux"
        ), '"SteamOS + Linux" checkbox isn\'t checked.'

        leader_page.click_on_the_lan_checkbox()
        assert self.is_checked(browser, "LAN"), '"(LAN)" checkbox isn\'t checked.'

        leader_page.click_on_the_action_checkbox()
        assert self.is_checked(browser, "action"), '"Action" checkbox isn\'t checked.'

        expected = leader_page.take_expected_count_of_action_games()
        actual = leader_page.take_actual_count_of_action_games()
        assert (
            expected == actual
        ), "Expected count of the action games doesn't equal actual."

        actual_game_name = leader_page.take_game_info("name")
        actual_game_date = leader_page.take_game_info("date")
        actual_game_price = leader_page.take_game_info("price")
        leader_page.click_on_the_first_game_field()
        assert self.is_page_open(
            browser, "game_page"
        ), "Can't open the first game page."

        game_page = GamePage(browser)
        expected_game_name = game_page.take_game_info("name")
        expected_game_date = game_page.take_game_info("date")
        expected_game_price = game_page.take_game_info("price")

        assert (
            actual_game_name == expected_game_name
        ), "Expected name of the first game doesn't equal actual."
        assert (
            actual_game_date == expected_game_date
        ), "Expected date of the first game doesn't equal actual."
        assert (
            actual_game_price == expected_game_price
        ), "Expected price of the first game doesn't equal actual."

    @staticmethod
    def is_page_open(browser, page):
        page_locators = {
            "main_page": SearchLocators.LOCATOR_MAIN_PAGE_UNIQUE_ELEMENT,
            "leader_page": SearchLocators.LOCATOR_LEADER_PAGE_UNIQUE_ELEMENT,
            "game_page": SearchLocators.LOCATOR_GAME_PAGE_UNIQUE_ELEMENT,
        }
        try:
            WebDriverWait(browser, TimeOut_default).until(
                EC.presence_of_element_located(page_locators[page])
            )
            return True
        except TimeoutException:
            return False

    @staticmethod
    def is_checked(browser, checkbox):
        checkbox_locators = {
            "linux": SearchLocators.LOCATOR_LINUX_CHECKBOX,
            "LAN": SearchLocators.LOCATOR_LAN_CHECKBOX,
            "action": SearchLocators.LOCATOR_ACTION_CHECKBOX,
        }
        try:
            WebDriverWait(browser, TimeOut_default).until(
                EC.presence_of_element_located(checkbox_locators[checkbox])
            )
            return True
        except TimeoutException:
            return False
