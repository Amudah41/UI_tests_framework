from task_2.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from task_2.config.config_data import TimeOut_quick


class SearchLocators:

    LOCATOR_LINUX_CHECKBOX = (
        By.XPATH,
        '//span[@data-value="linux"]//span[@class="tab_filter_control_checkbox"]',
    )

    LOCATOR_GAMERS_FIELD = (By.XPATH, '//div[@data-collapse-name="category3"]')
    LOCATOR_LAN_CHECKBOX = (
        By.XPATH,
        '//div[@data-value="48"]//span[contains(@class,"checkbox")]',
    )

    LOCATOR_FLAG_ELEMENT_1 = (
        By.XPATH,
        '//div[@class="search_results_filtered_warning collapsed"]',
    )
    LOCATOR_SHOW_ALL_MARKERS_BUTTON = (
        By.XPATH,
        '//a[contains(@onclick, "TagFilter_Container")]',
    )
    LOCATOR_EXPECTED_ACTION_FIELD = (
        By.XPATH,
        '//div[@data-value="19"]//span[contains(@class,"tab_filter_control_count")]',
    )
    LOCATOR_ACTION_CHECKBOX = (
        By.XPATH,
        '//div[@data-value="19"]//span[contains(@class,"tab_filter_control_checkbox")]',
    )

    LOCATOR_FLAG_ELEMENT_2 = (
        By.XPATH,
        '//div[@id="search_results"]//div[contains(@style,"opacity")]',
    )
    LOCATOR_FLAG_ELEMENT_3 = (
        By.XPATH,
        '//div[@id="search_result_container" and not(contains(@style,"opacity"))]',
    )
    LOCATOR_ACTUAL_ACTION_FIELD = (By.XPATH, '//div[@class="search_results_count"]')

    LOCATOR_EXPECTED_GAME_NAME_FIELD = (
        By.XPATH,
        '//div[@id="search_resultsRows"]//a[1]//span[@class="title"]',
    )
    LOCATOR_EXPECTED_GAME_DATE_FIELD = (
        By.XPATH,
        '//div[@id="search_resultsRows"]//a[1]//div[contains(@class,"search_released")]',
    )
    LOCATOR_EXPECTED_GAME_PRICE_FIELD = (
        By.XPATH,
        '//div[@id="search_resultsRows"]//a[1]//div[contains(@class,"search_price")]',
    )
    LOCATOR_GAME_FIELD = (By.XPATH, '//div[@id="search_resultsRows"]//a[1]')


class LeaderPage(BasePage):
    def click_on_the_linux_checkbox(self):
        return self.find_element(
            SearchLocators.LOCATOR_LINUX_CHECKBOX, time=TimeOut_quick
        ).click()

    def click_on_the_lan_checkbox(self):
        self.find_element(SearchLocators.LOCATOR_GAMERS_FIELD).click()
        return self.find_element(SearchLocators.LOCATOR_LAN_CHECKBOX).click()

    def click_on_the_action_checkbox(self):
        self.find_element(SearchLocators.LOCATOR_FLAG_ELEMENT_1)
        self.find_element(SearchLocators.LOCATOR_SHOW_ALL_MARKERS_BUTTON).click()
        self.expected_action_count = self.find_element(
            SearchLocators.LOCATOR_EXPECTED_ACTION_FIELD
        ).text
        return self.find_element(SearchLocators.LOCATOR_ACTION_CHECKBOX).click()

    def take_expected_count_of_action_games(self):
        return self.expected_action_count

    def take_actual_count_of_action_games(self):
        self.find_element(SearchLocators.LOCATOR_FLAG_ELEMENT_2)
        self.find_element(SearchLocators.LOCATOR_FLAG_ELEMENT_3)

        return self.find_element(
            SearchLocators.LOCATOR_ACTUAL_ACTION_FIELD
        ).text.split()[-1][:-1]

    def take_game_info(self, aspect):
        info = {
            "name": SearchLocators.LOCATOR_EXPECTED_GAME_NAME_FIELD,
            "date": SearchLocators.LOCATOR_EXPECTED_GAME_DATE_FIELD,
            "price": SearchLocators.LOCATOR_EXPECTED_GAME_PRICE_FIELD,
        }
        return self.find_element(info[aspect], time=TimeOut_quick).text

    def click_on_the_first_game_field(self):
        return self.find_element(SearchLocators.LOCATOR_GAME_FIELD).click()
