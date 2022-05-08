import pytest  # noqa
from task_3.task.pages.MainPage import MainPage
from task_3.task.pages.AlertPage import AlertPage
from selenium.common.exceptions import NoAlertPresentException
from task_3.framework.utils.Utils import StringUtils


class TestCase1:
    def test_case_1(self, browser):
        main_page = MainPage()
        assert main_page.is_loaded(), "Main page is not loaded."
        main_page.click_on_the_alert_frame_and_windows_page_button()

        alert_page = AlertPage()

        alert_page.click_on_the_left_form_alert_button()
        # browser.scroll_page_up()
        assert alert_page.is_loaded(), "Alert page is not loaded."

        alert_page.click_on_the_alert_button()

        alert = browser.switch_to_alert()
        assert (
            alert.text == "You clicked a button"
        ), "Alert text is not 'You clicked a button'."
        alert.accept()
        try:
            browser.switch_to_alert()
            assert False, "Alert don't close"
        except NoAlertPresentException:
            assert True

        alert_page.click_on_the_alert_confirm_button()
        alert = browser.switch_to_alert()
        alert.accept()
        try:
            browser.switch_to_alert()
            assert False, "Alert don't close"
        except NoAlertPresentException:
            assert True
        assert (
            alert_page.take_text_after_confirm_alert() == "You selected Ok"
        ), "Alert text is not 'You selected Ok'."

        alert_page.click_on_the_alert_promt_button()
        alert = browser.switch_to_alert()
        assert (
            alert.text == "Please enter your name"
        ), "Alert text is not 'Please enter your name'."
        text = StringUtils.random_string
        browser.write_text_to_alert_text_field(text)

        alert.accept()
        try:
            browser.switch_to_alert()
            assert False, "Alert don't close"
        except NoAlertPresentException:
            assert True
        assert (
            alert_page.take_text_after_promt_alert() == f"You entered {text}"
        )
