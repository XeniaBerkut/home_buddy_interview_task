from selenium.webdriver.chrome.webdriver import WebDriver

from src.helpers.test_data_helpers import make_email_unique, expected_thanks_text, create_unique_phone_number
from src.ui.pages.home_page import HomePage


# TODO rename the test
def test_positive_first(driver: WebDriver, logger):
    zip_code = 10001
    project_type = 'replacement'
    equipment = 'air_conditioner', 'boiler'
    equipment_age = 'older_than_10'
    fuel = 'oil'
    property_type = 'detached'
    square_feet = 340
    name = 'Johan Frame'
    email = make_email_unique('j.frame@gmail.com')
    phone_number = create_unique_phone_number()

    home_page: HomePage = HomePage(driver, logger)

    logger.info(f'Fill zip_code {zip_code} and start estimation')
    home_page.fill_zip_code(zip_code)
    project_questionnaire_form = home_page.submit_zip_code()

    logger.info(f'Select project type {project_type}')
    project_questionnaire_form.select_project_type(project_type)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select equipment {equipment}')
    project_questionnaire_form.select_equipment_type(equipment)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select HVAC system fuel {fuel}')
    project_questionnaire_form.select_hvac_system_fuel(fuel)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select equipment age {equipment_age}')
    project_questionnaire_form.select_equipment_age(equipment_age)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select property type {property_type}')
    project_questionnaire_form.select_property_type(property_type)
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill square feet with {square_feet}')
    project_questionnaire_form.fill_square_feet(square_feet)
    project_questionnaire_form.click_next_button()

    logger.info(f'Mark as homeowner')
    project_questionnaire_form.mark_as_homeowner()
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill full name and email fields with {name}, {email}')
    project_questionnaire_form.fill_full_name(name)
    project_questionnaire_form.fill_email(email)
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill phone number field with {phone_number}')
    project_questionnaire_form.fill_phone_number(phone_number)
    project_questionnaire_form.click_next_button()
    thank_you_page = project_questionnaire_form.click_confirm_button()

    expected_text = expected_thanks_text(name)
    actual_text = thank_you_page.get_thanks_text()

    assert actual_text == expected_text, f'Expected {expected_text}, but was {actual_text}'
    assert thank_you_page.driver.current_url == 'https://hb-autotests.stage.sirenltd.dev/thank-you'
