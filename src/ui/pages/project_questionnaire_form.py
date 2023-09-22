from selenium.webdriver.common.by import By

from src.ui.pages.base_page import BasePage
from src.ui.pages.thank_you_page import ThankYouPage


class ProjectQuestionnaireForm(BasePage):
    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    locators = {
        'replacement': (By.XPATH, "//span[contains(text(),'Replacement')]"),
        'repair': (By.XPATH, "//span[contains(text(),'Repair')]"),
        'air_conditioner': (By.XPATH, "//span[contains(text(),'Air conditioner')]"),
        'central_heating': (By.XPATH, "//span[contains(text(),'Central heating')]"),
        'boiler': (By.XPATH, "//span[contains(text(),'Boiler')]"),
        'heat_pump': (By.XPATH, "//span[contains(text(),'Heat pump')]"),
        'water_heater': (By.XPATH, "//span[contains(text(),'Water heater')]"),
        'gas': (By.XPATH, "//span[contains(text(),'Gas')]"),
        'electricity': (By.XPATH, "//span[contains(text(),'Electricity')]"),
        'propane': (By.XPATH, "//span[contains(text(),'Propane')]"),
        'oil': (By.XPATH, "//span[contains(text(),'Oil')]"),
        'less_than_5': (By.XPATH, "//span[contains(text(),'Less than 5')]"),
        'between_5_and_10': (By.XPATH, "//span[contains(text(),'5 to 10')]"),
        'older_than_10': (By.XPATH, "//span[contains(text(),'Older than 10')]"),
        'detached': (By.XPATH, "//span[contains(text(),'Detached')]"),
        'mobile': (By.XPATH, "//span[contains(text(),'Mobile')]"),
        'commercial': (By.XPATH, "//span[contains(text(),'Commercial')]"),
        'condominium': (By.XPATH, "//span[contains(text(),'Apartment')]"),
        'square_feet': (By.ID, 'squareFeet'),
        'home_owner_true': (By.XPATH, "//span[contains(text(),'Yes')]"),
        'full_name': (By.ID, 'fullName'),
        'email': (By.ID, 'email'),
        'phone': (By.ID, 'phoneNumber'),
        'phone_confirmation_header': (By.XPATH, "//h4[contains(text(), 'Please confirm your phone number.')]"),
        'not_sure': (By.XPATH, "//span[contains(text(),'Not sure')]"),
        'submit': (By.XPATH, "//button[@type='submit']")
    }

    def select_project_type(self, project_type):
        self.driver.find_element(*self.locators[project_type]).click()

    def click_next_button(self):
        self.driver.find_element(*self.locators['submit']).click()

    def select_equipment_type(self, equipment):
        for item in equipment:
            self.driver.find_element(*self.locators[item]).click()

    def select_hvac_system_fuel(self, fuel):
        self.driver.find_element(*self.locators[fuel]).click()

    def select_equipment_age(self, age):
        self.driver.find_element(*self.locators[age]).click()

    def select_property_type(self, property_type):
        self.driver.find_element(*self.locators[property_type]).click()

    def fill_square_feet(self, square_feet):
        self.driver.find_element(*self.locators['square_feet']).send_keys(square_feet)

    def mark_as_homeowner(self):
        self.driver.find_element(*self.locators['home_owner_true']).click()

    def fill_full_name(self, name):
        self.driver.find_element(*self.locators['full_name']).send_keys(name)

    def fill_email(self, email):
        self.driver.find_element(*self.locators['email']).send_keys(email)

    def fill_phone_number(self, phone):
        self.driver.find_element(*self.locators['phone']).send_keys(phone)

    def click_submit_button(self):
        self.driver.find_element(*self.locators['submit']).click()
        thank_you_page = ThankYouPage(self.driver, self.logger)
        thank_you_page.wait_thank_you_form()
        return thank_you_page

    def click_confirm_button(self):
        self.wait_element_is_located(self.locators['phone_confirmation_header'])
        self.driver.find_element(*self.locators['submit']).click()
        thank_you_page = ThankYouPage(self.driver, self.logger)
        thank_you_page.wait_thank_you_form()
        return thank_you_page
