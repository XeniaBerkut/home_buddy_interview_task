from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    locators = {
        'zip_code_header': (By.ID, "zipCode"),
        'header_form': (By.ID, "zip_header"),
        'submit_btn_header': (By.TAG_NAME, "BUTTON")
    }

    def fill_zip_code(self, zip_code):
        self.logger.info("Fill zip code")
        self.driver.find_element(*self.locators['zip_code_header']).send_keys(zip_code)

    def submit_zip_code(self):
        self.logger.info("Click submit button")
        parent_element = self.driver.find_element(*self.locators['header_form'])
        parent_element.find_element(*self.locators['submit_btn_header']).click()