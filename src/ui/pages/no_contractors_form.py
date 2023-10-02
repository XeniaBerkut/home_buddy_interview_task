from logging import Logger

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from src.ui.pages.base_page import BasePage


class NoContractorsForm(BasePage):
    def __init__(self, driver: WebDriver, logger: Logger):
        super().__init__(driver, logger)

    locators = {
        'no_contractors_text': (By.XPATH, "//h4[contains(text(), "
                                          "'Unfortunately, I have no matching contractors in your area yet.')]"),
        'email': (By.ID, 'email'),
        'submit': (By.XPATH, "//button[@type='submit']"),
        'header': (By.TAG_NAME, "h4"),
        'try_button': (By.XPATH, "//span[contains(text(),'Try another ZIP Code')]")
    }

    def fill_email(self, email: str):
        self.wait_element_is_located(self.locators['no_contractors_text'])
        self.driver.find_element(*self.locators['email']).send_keys(email)

    def click_next_button(self):
        self.driver.find_element(*self.locators['submit']).click()

    def get_header_text(self) -> str:
        self.wait_element_is_located(self.locators['try_button'])
        return self.driver.find_element(*self.locators['header']).text
