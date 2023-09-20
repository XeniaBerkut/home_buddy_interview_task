from logging import Logger
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, logger: Logger):
        super().__init__()
        self.driver = driver
        self.logger = logger
