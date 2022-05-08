import pytest  # noqa
from task_3.task.pages.MainPage import MainPage
from task_3.task.pages.NestedFramesPage import NestedFramesPage


class TestCase2:
    def test_case_2(self, browser):
        main_page = MainPage()
        assert main_page.is_loaded(), "Main page isn't loaded."

        main_page.click_on_the_alert_frame_and_windows_page_button()

        nested_frames_page = NestedFramesPage()

        nested_frames_page.click_on_the_left_form_nested_frames_button()
        assert (
            nested_frames_page.is_loaded()
        ), "Nested frames page is not loaded."

        browser.switch_to_frame("frame1")
        browser.switch_to_frame(0)
        assert (
            nested_frames_page.take_iframe_text(2) == "Child Iframe"
        ), 'There is no "Child Iframe"'

        browser.switch_to_parent_frame()
        assert (
            nested_frames_page.take_iframe_text(1) == "Parent frame"
        ), 'There is no "Parent frame"'

        browser.switch_to_default_content()
        nested_frames_page.click_on_the_left_form_frames_button()

        browser.switch_to_frame("frame1")
        text_1 = nested_frames_page.take_iframe_text(3)
        browser.switch_to_parent_frame()
        browser.switch_to_frame("frame2")
        text_2 = nested_frames_page.take_iframe_text(4)
        assert text_1 == text_2
