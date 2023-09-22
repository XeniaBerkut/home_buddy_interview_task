from logging import Logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from src.ui.pages.base_page import BasePage


class ThankYouPage(BasePage):
    def __init__(self, driver: WebDriver, logger: Logger):
        super().__init__(driver, logger)

    locators = {
        'thank_you_form': (By.ID, 'StepBodyId'),
        'personalised_text': (By.TAG_NAME, 'h4')
    }

    def get_thanks_text(self) -> str:
        parent = self.driver.find_element(*self.locators['thank_you_form'])
        return parent.find_element(*self.locators['personalised_text']).text

    def wait_thank_you_form(self):
        WebDriverWait(self.driver, 10).until(EC.title_is('Thank you - HomeBuddy'))
