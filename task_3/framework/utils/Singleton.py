from task_3.framework.utils.BrowserFactory import BrowserFactory
from task_3.framework.utils.Loger import Loger


class Singleton:
    class __Singleton:
        def __init__(self, browser_name):
            self.driver = BrowserFactory().get_driver(browser_name)

        def refresh(self, browser_name):
            self.driver = BrowserFactory().get_driver(browser_name)

    __driver = None
    is_closed = False

    def __init__(self, browser_name="chrome"):
        self.browser_name = browser_name
        Loger().log(f"Browser {self.browser_name} is used.")

        if not Singleton.__driver:
            Loger().log(f"Take new {self.browser_name} driver.")
            Singleton._Singleton__driver = Singleton.__Singleton(
                self.browser_name
            ).driver
        elif Singleton.is_closed:
            Loger().log(f"Refresh {self.browser_name} driver.")
            Singleton._Singleton__driver = Singleton.__Singleton(
                self.browser_name
            ).driver

    @classmethod
    def get_driver(cls):
        return cls.__driver
