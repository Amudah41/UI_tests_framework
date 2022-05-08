from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options  # noqa
from task_3.framework.config.ConfigManager import ConfigManager
from task_3.framework.errors.Errors import NoSuchElementError


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name):
        options = Options()
        # options.add_argument("--headless")
        size = ConfigManager().take_conf_param("WINDOW_SIZE")
        options.add_argument(f"--window-size={size}")
        if browser_name == "chrome":
            s = Service(ChromeDriverManager().install())
            return webdriver.Chrome(options=options, service=s)
        if browser_name == "firefox":
            return webdriver.Firefox(
                options=options, executable_path=GeckoDriverManager().install()
            )
        raise NoSuchElementError(f"Browser {browser_name} is not supported.")
