from task_2.pages.BasePage import BasePage
from task_2.utils.utils import StringUtils
from selenium.webdriver.common.by import By
from task_2.config.config_data import TimeOut_quick


class SearchLocators:
    LOCATOR_ONLINE_GAMERS_FIELD = (By.XPATH, "//div[@class='online_stat'][1]")
    LOCATOR_IN_GAME_GAMERS_FIELD = (By.XPATH, "//div[@class='online_stat'][2]")
    LOCATOR_MAIN_PAGE_BUTTON = (
        By.XPATH,
        '//div[@class="supernav_container"]//a[@data-tooltip-content=".submenu_store"]',
    )


class AboutPage(BasePage):
    def take_count_of_gamers(self, type):
        gamers_types = {
            "online": SearchLocators.LOCATOR_ONLINE_GAMERS_FIELD,
            "in_game": SearchLocators.LOCATOR_IN_GAME_GAMERS_FIELD,
        }
        gamers = self.find_element(gamers_types[type], time = TimeOut_quick).text.split()[
            -1
        ]
        return StringUtils.convert_string_to_int(gamers)

    def click_on_the_about_page_button(self):
        return self.find_element(
            SearchLocators.LOCATOR_ABOUT_PAGE_BUTTON, time = TimeOut_quick
        ).click()

    def click_on_the_main_page_button(self):
        return self.find_element(
            SearchLocators.LOCATOR_MAIN_PAGE_BUTTON, time = TimeOut_quick
        ).click()
