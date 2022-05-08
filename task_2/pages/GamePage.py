from task_2.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from task_2.config.config_data import TimeOut_quick


class SearchLocators:
    LOCATOR_ACTUAL_GAME_NAME_FIELD = (By.XPATH, '//div[@id="appHubAppName"]')
    LOCATOR_ACTUAL_GAME_DATE_FIELD = (
        By.XPATH,
        '//div[@class="release_date"]//div[@class="date"]',
    )
    LOCATOR_ACTUAL_GAME_PRICE_FIELD = (
        By.XPATH,
        '//div[contains(@id,"game_area_purchase_section")]//div[contains(@class, "price")]',
    )


class GamePage(BasePage):
    def take_game_info(self, aspect):
        info = {
            "name": SearchLocators.LOCATOR_ACTUAL_GAME_NAME_FIELD,
            "date": SearchLocators.LOCATOR_ACTUAL_GAME_DATE_FIELD,
            "price": SearchLocators.LOCATOR_ACTUAL_GAME_PRICE_FIELD,
        }
        return self.find_element(info[aspect], time=TimeOut_quick).text
