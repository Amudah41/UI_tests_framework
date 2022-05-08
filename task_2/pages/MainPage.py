from task_2.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from task_2.config.config_data import TimeOut_quick


class SearchLocators:
    LOCATOR_ABOUT_PAGE_BUTTON = (
        By.XPATH,
        "//div[@class='supernav_container']//a[@class='menuitem'][1]",
    )
    LOCATOR_DROP_DOWN_MENU_FIELD = (
        By.XPATH,
        "//div[@id='noteworthy_tab']//span[@class='pulldown']",
    )
    LOCATOR_LEADER_BUTTON = (By.XPATH, '//div[@id="noteworthy_flyout"]//a[1]')


class MainPage(BasePage):
    def click_on_the_about_page_button(self):
        return self.find_element(
            SearchLocators.LOCATOR_ABOUT_PAGE_BUTTON, time=TimeOut_quick
        ).click()

    def click_on_the_leader_page_button(self):
        self.move_to_element(
            self.find_element(SearchLocators.LOCATOR_DROP_DOWN_MENU_FIELD)
        )
        return self.find_visible_element(SearchLocators.LOCATOR_LEADER_BUTTON).click()
