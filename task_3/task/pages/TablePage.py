from task_3.framework.pages.BaseForm import BaseForm
from selenium.webdriver.common.by import By
from task_3.task.elements.Button import Button
from task_3.task.elements.TextField import TextField
from task_3.task.elements.Table import Table
from task_3.framework.config.ConfigManager import ConfigManager
from task_3.framework.utils.Utils import StringUtils


class TablePageLocators:
    LOCATOR_TABLE_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//div[contains(@class, 'web-tables') ]//button[@id='addNewRecordButton']",
    )
    LOCATOR_LEFT_FORM_WEB_TABLES_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"element-list") and contains(@class,"show")]//li[@id="item-3"]',
    )
    LOCATOR_ADD_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'web-tables') ]//button[@id='addNewRecordButton']",
    )
    LOCATOR_REGISTRATION_FORM_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']",
    )
    LOCATOR_WEB_TABLE = (By.XPATH, "//div[contains(@class, 'ReactTable')]")
    LOCATOR_TOTAL_TABLE_PAGES = (
        By.XPATH,
        "//div[contains(@class, 'ReactTable')]//span[contains(@class, 'totalPages')]",
    )
    LOCATOR_SET_PAGE_NUMBER_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'ReactTable')]//div[contains(@class, 'pageJump')]//input",
    )
    LOCATOR_REGISTRATION_FORM_FIRST_NAME_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//input[@id='firstName']",
    )
    LOCATOR_REGISTRATION_FORM_LAST_NAME_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//input[@id='lastName']",
    )
    LOCATOR_REGISTRATION_FORM_EMAIL_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//input[@id='userEmail']",
    )
    LOCATOR_REGISTRATION_FORM_AGE_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//input[@id='age']",
    )
    LOCATOR_REGISTRATION_FORM_SALARY_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//input[@id='salary']",
    )
    LOCATOR_REGISTRATION_FORM_DEPARTMENT_FIELD = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//input[@id='department']",
    )
    LOCATOR_REGISTRATION_FORM_SUBMIT_BUTTON = (
        By.XPATH,
        "//div[@class='modal-body']//form[@id='userForm']//button[@id='submit']",
    )
    LOCATOR_WEB_TABLE_RAWS = (
        By.XPATH,
        "//div[contains(@class, 'ReactTable')]//div[contains(@class, 'tbody')]//div[@role='row']",
    )


class TablePage(BaseForm):

    LOCATOR_WEB_TABLE_DELETE_RECORD_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'ReactTable')]//div[contains(@class, 'tbody')]//div[@role='rowgroup']//span[@id='delete-record-%s']",
    )

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            TablePageLocators.LOCATOR_TABLE_PAGE_UNIQUE_ELEMENT,
        )
        self.web_tables_button = Button(
            "left form web tables button",
            TablePageLocators.LOCATOR_LEFT_FORM_WEB_TABLES_BUTTON,
        )
        self.add_button = Button(
            "add button",
            TablePageLocators.LOCATOR_ADD_BUTTON,
        )
        self.web_table = Table(
            "Web table", TablePageLocators.LOCATOR_WEB_TABLE
        )
        self.total_pages_field = TextField(
            "total pages field", TablePageLocators.LOCATOR_TOTAL_TABLE_PAGES
        )
        self.set_pages_field = TextField(
            "set page field", TablePageLocators.LOCATOR_SET_PAGE_NUMBER_FIELD
        )

        self.first_name_field = TextField(
            "first name field",
            TablePageLocators.LOCATOR_REGISTRATION_FORM_FIRST_NAME_FIELD,
        )

        self.last_name_field = TextField(
            "last name field",
            TablePageLocators.LOCATOR_REGISTRATION_FORM_LAST_NAME_FIELD,
        )

        self.email_field = TextField(
            "Email field",
            TablePageLocators.LOCATOR_REGISTRATION_FORM_EMAIL_FIELD,
        )

        self.age_field = TextField(
            "age field", TablePageLocators.LOCATOR_REGISTRATION_FORM_AGE_FIELD
        )

        self.salary_field = TextField(
            "salary field",
            TablePageLocators.LOCATOR_REGISTRATION_FORM_SALARY_FIELD,
        )

        self.department_field = TextField(
            "department field",
            TablePageLocators.LOCATOR_REGISTRATION_FORM_DEPARTMENT_FIELD,
        )

        self.submit_button = Button(
            "submit button",
            TablePageLocators.LOCATOR_REGISTRATION_FORM_SUBMIT_BUTTON,
        )

    def click_on_the_left_form_web_tables_button(self):

        self.scroll_page_down_ot_element(self.web_tables_button)
        self.web_tables_button.click()

    def click_on_the_add_button(self):
        self.add_button.click()

    def find_the_first_pad_raw_num_and_its_page_num(self):

        total_pages = StringUtils.convert_string_to_int(
            self.total_pages_field.text()
        )
        self.set_pages_field.click_and_write_text(total_pages)

        raws = self.web_table.find_elements(
            TablePageLocators.LOCATOR_WEB_TABLE_RAWS
        )

        for raw_num, raw in enumerate(raws):
            if raw.text == "       ":
                return total_pages, raw_num
        return total_pages + 1, 0

    def read_raw_from_csv(self, user_number=""):
        user_raw = ConfigManager().take_table_raw(user_number)
        return user_raw

    def fill_in_the_form_fields(self, raw):
        self.first_name_field.click_and_write_text(raw["First Name"])
        self.last_name_field.click_and_write_text(raw["Last Name"])
        self.email_field.click_and_write_text(raw["Email"])
        self.age_field.click_and_write_text(raw["Age"])
        self.salary_field.click_and_write_text(raw["Salary"])
        self.department_field.click_and_write_text(raw["Department"])
        self.submit_button.click()

    def take_add_user_raw(self, page_num, raw_num):

        self.set_pages_field.click_and_write_text(page_num)

        return self.web_table.find_elements(
            TablePageLocators.LOCATOR_WEB_TABLE_RAWS
        )[raw_num].text

    @staticmethod
    def raws_are_equal(expected_raw, actual_raw):
        return all(
            (
                expected_raw["First Name"] == actual_raw[0],
                expected_raw["Last Name"] == actual_raw[1],
                expected_raw["Age"] == actual_raw[2],
                expected_raw["Email"] == actual_raw[3],
                expected_raw["Salary"] == actual_raw[4],
                expected_raw["Department"] == actual_raw[5],
            )
        )

    def delete_added_user(self, page_num, raw_num):
        self.set_pages_field.click_and_write_text(page_num)

        Button(
            f"delete {raw_num} record button.",
            (
                self.LOCATOR_WEB_TABLE_DELETE_RECORD_BUTTON[0],
                self.LOCATOR_WEB_TABLE_DELETE_RECORD_BUTTON[1] % raw_num,
            ),
        ).click()

    def is_added_user_deleted(self, page_num, raw_num):
        self.set_pages_field.click_and_write_text(page_num)

        raws = self.web_table.find_elements(
            TablePageLocators.LOCATOR_WEB_TABLE_RAWS
        )
        return raws[raw_num].text == "       "
