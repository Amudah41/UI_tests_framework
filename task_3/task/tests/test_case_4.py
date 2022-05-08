import pytest  # noqa
from task_3.task.pages.MainPage import MainPage
from task_3.task.pages.BrowserWindowPage import BrowserWindowPage
from task_3.task.pages.SamplePage import SamplePage


class TestCase4:
    def test_case_4(self, browser):
        main_page = MainPage()
        assert main_page.is_loaded(), "Main page is not loaded."

        main_page.click_on_the_alert_frame_and_windows_page_button()
        browser_window_page = BrowserWindowPage()
        browser_window_page.click_on_the_left_form_browser_windows_button()

        assert (
            browser_window_page.is_loaded()
        ), "Browser Window page is not loaded."

        browser_window_page.click_on_the_new_tab_button()

        browser.switch_to_window(1)

        assert SamplePage().is_loaded(), "New tab is not open."
        browser.close()
        browser.switch_to_window(0)
        assert (
            browser_window_page.is_loaded()
        ), "Browser Window page is not loaded."
