from selenium.webdriver.chrome.options import Options

WindowSize_LEN = 1920
WindowSize_HIGH = 1080

WINDOW_SIZE = "1920,1080"

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=%s" % WINDOW_SIZE)


TimeOut_default = 5
TimeOut_quick = 2
