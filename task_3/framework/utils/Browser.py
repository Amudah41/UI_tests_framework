from task_3.framework.utils.Singleton import Singleton
from task_3.framework.utils.Utils import StringUtils
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from task_3.framework.config.config_data import TimeOut_default
from task_3.framework.utils.Loger import Loger


class Browser(Singleton):
    def get(self, link):
        Loger().log(f"Get page from link {link}.")
        browser = Browser.get_driver()
        return browser.get(link)

    def close(self):
        Loger().log("Close the current tab.")
        browser = Browser.get_driver()
        return browser.close()

    def quit(self):
        Loger().log("Quit the driver.")
        Singleton.is_closed = True
        browser = Browser.get_driver()

        browser.quit()

    @classmethod
    def scroll_page_down_until_element_not_visible(cls, locator):
        browser = Browser.get_driver()
        element = WebDriverWait(browser, TimeOut_default).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        browser.execute_script("arguments[0].scrollIntoView(true);", element)

    @classmethod
    def scroll_page_up(cls):
        browser = Browser.get_driver()

        browser.execute_script(
            "window.scrollTo(document.body.scrollHeight, 0);"
        )

    def switch_to_alert(self):
        Loger().log("Switch to alert.")
        browser = Browser.get_driver()

        return browser.switch_to.alert

    def switch_to_frame(self, frame_id):
        Loger().log(f"Swith to frame {frame_id}.")
        browser = Browser.get_driver()

        return browser.switch_to.frame(frame_id)

    def switch_to_default_content(self):
        Loger().log("Switch to default content.")
        browser = Browser.get_driver()

        return browser.switch_to.default_content()

    def switch_to_parent_frame(self):
        Loger().log("Switch to parent frame.")
        browser = Browser.get_driver()

        return browser.switch_to.parent_frame()

    def write_text_to_alert_text_field(self):
        Loger().log("Write text to the alert text field.")
        self.text = StringUtils.random_string()
        browser = Browser.get_driver()
        alert = Alert(browser)
        return alert.send_keys(self.text)

    def take_written_text_to_alert(self):
        Loger().log("Take written text to alert.")
        return self.text

    def write_text(self, text):
        Loger().log("Write text to the text field.")
        browser = Browser.get_driver()
        browser.send_keys(text)

    def switch_to_window(self, id):
        browser = Browser.get_driver()
        return browser.switch_to.window(browser.window_handles[id])
