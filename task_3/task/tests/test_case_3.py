import pytest  # noqa
from task_3.task.pages.MainPage import MainPage
from task_3.task.pages.TablePage import TablePage


class TestCase3:
    def test_case_3(self, browser):
        main_page = MainPage()
        assert main_page.is_loaded(), "Main page isn't loaded."

        main_page.click_on_the_elements_page_button()
        table_page = TablePage()

        table_page.click_on_the_left_form_web_tables_button()
        assert table_page.is_loaded(), "Table page is not loaded."

        table_page.click_on_the_left_form_web_tables_button()
        (
            page_num,
            raw_num,
        ) = table_page.find_the_first_pad_raw_num_and_its_page_num()

        table_page.click_on_the_add_button()

        expected_raw = table_page.read_raw_from_csv(user_number="1")
        table_page.fill_in_the_form_fields(expected_raw)
        actual_raw = table_page.take_add_user_raw(page_num, raw_num).split(
            "\n"
        )
        assert table_page.raws_are_equal(
            expected_raw, actual_raw
        ), f"User {expected_raw['First Name']} {expected_raw['Last Name']} is not added."

        table_page.delete_added_user(page_num, raw_num)
        assert table_page.is_added_user_deleted(
            page_num, raw_num
        ), f"User {expected_raw['First Name']} {expected_raw['Last Name']} is not deleted."
