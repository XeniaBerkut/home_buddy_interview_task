from logging import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, logger: Logger):
        super().__init__()
        self.driver = driver
        self.logger = logger

    def wait_element_is_located(self, element_locator: tuple):
        self.logger.info(f"Wait for {element_locator} to be visible")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(element_locator))
        self.logger.info("Element is located")
