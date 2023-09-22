import os
from logging import Logger

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from src.helpers.test_data_helpers import make_email_unique, expected_thanks_text, create_unique_phone_number, \
    get_test_data_from_json
from src.ui.entities.project import Project
from src.ui.enums.urls import URLS
from src.ui.pages.home_page import HomePage

data_valid_phone: dict = get_test_data_from_json(os.path.join(
    os.path.dirname(__file__),
    "data_get_estimate_valid_phone_number.json"))


@pytest.mark.parametrize("test_case",
                         data_valid_phone,
                         ids=[data["test_case_title"] for data in data_valid_phone])
def test_get_estimate_valid_phone_number(driver: WebDriver, logger: Logger, test_case: dict):
    test_case["data"]["email"] = make_email_unique(test_case["data"]["email"])
    test_case["data"]["phone_number"] = create_unique_phone_number(test_case["data"]["state_code"])

    project = Project(**test_case["data"])

    home_page: HomePage = HomePage(driver, logger)

    logger.info(f'Fill zip_code {project.zip_code} and start estimation')
    home_page.fill_zip_code(project.zip_code)
    project_questionnaire_form = home_page.submit_zip_code()

    logger.info(f'Select project type {project.project_type}')
    project_questionnaire_form.select_project_type(project.project_type)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select equipment {project.equipment}')
    project_questionnaire_form.select_equipment_type(project.equipment)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select HVAC system fuel {project.fuel}')
    project_questionnaire_form.select_hvac_system_fuel(project.fuel)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select equipment age {project.equipment_age}')
    project_questionnaire_form.select_equipment_age(project.equipment_age)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select property type {project.property_type}')
    project_questionnaire_form.select_property_type(project.property_type)
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill square feet with {project.square_feet}')
    project_questionnaire_form.fill_square_feet(project.square_feet)
    project_questionnaire_form.click_next_button()

    logger.info(f'Mark as homeowner')
    project_questionnaire_form.mark_as_homeowner()
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill full name and email fields with {project.name}, {project.email}')
    project_questionnaire_form.fill_full_name(project.name)
    project_questionnaire_form.fill_email(project.email)
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill phone number field with {project.phone_number}')
    project_questionnaire_form.fill_phone_number(project.phone_number)
    thank_you_page = project_questionnaire_form.click_submit_button()

    expected_text = expected_thanks_text(project.name)
    actual_text = thank_you_page.get_thanks_text()

    assert actual_text == expected_text, f'Expected {expected_text}, but was {actual_text}'
    assert thank_you_page.driver.current_url == URLS.THANK_YOU_PAGE.value


data_invalid_phone: dict = get_test_data_from_json(os.path.join(
    os.path.dirname(__file__),
    "data_get_estimate_invalid_phone_number.json"))


@pytest.mark.parametrize("test_case",
                         data_invalid_phone,
                         ids=[data["test_case_title"] for data in data_invalid_phone])
def test_get_estimate_invalid_phone_number(driver: WebDriver, logger: Logger, test_case: dict):
    test_case["data"]["email"] = make_email_unique(test_case["data"]["email"])
    test_case["data"]["phone_number"] = create_unique_phone_number(test_case["data"]["state_code"])

    project = Project(**test_case["data"])

    home_page: HomePage = HomePage(driver, logger)

    logger.info(f'Fill zip_code {project.zip_code} and start estimation')
    home_page.fill_zip_code(project.zip_code)
    project_questionnaire_form = home_page.submit_zip_code()

    logger.info(f'Select project type {project.project_type}')
    project_questionnaire_form.select_project_type(project.project_type)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select equipment {project.equipment}')
    project_questionnaire_form.select_equipment_type(project.equipment)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select HVAC system fuel {project.fuel}')
    project_questionnaire_form.select_hvac_system_fuel(project.fuel)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select equipment age {project.equipment_age}')
    project_questionnaire_form.select_equipment_age(project.equipment_age)
    project_questionnaire_form.click_next_button()

    logger.info(f'Select property type {project.property_type}')
    project_questionnaire_form.select_property_type(project.property_type)
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill square feet with {project.square_feet}')
    project_questionnaire_form.fill_square_feet(project.square_feet)
    project_questionnaire_form.click_next_button()

    logger.info(f'Mark as homeowner')
    project_questionnaire_form.mark_as_homeowner()
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill full name and email fields with {project.name}, {project.email}')
    project_questionnaire_form.fill_full_name(project.name)
    project_questionnaire_form.fill_email(project.email)
    project_questionnaire_form.click_next_button()

    logger.info(f'Fill phone number field with {project.phone_number}')
    project_questionnaire_form.fill_phone_number(project.phone_number)
    project_questionnaire_form.click_next_button()
    thank_you_page = project_questionnaire_form.click_confirm_button()

    expected_text = expected_thanks_text(project.name)
    actual_text = thank_you_page.get_thanks_text()

    assert actual_text == expected_text, f'Expected {expected_text}, but was {actual_text}'
    assert thank_you_page.driver.current_url == URLS.THANK_YOU_PAGE.value


def test_zip_without_contractors(driver: WebDriver, logger: Logger):
    data_zip: dict = get_test_data_from_json(os.path.join(
        os.path.dirname(__file__),
        "data_zip_without_contractors.json"))

    home_page: HomePage = HomePage(driver, logger)

    logger.info(f'Fill zip_code {data_zip["zip_code"]} and go further')
    home_page.fill_zip_code(data_zip["zip_code"])
    no_contractors_form = home_page.submit_zip_code_no_contractors()
    no_contractors_form.fill_email(data_zip["email"])
    no_contractors_form.click_next_button()
    assert no_contractors_form.get_header_text() == data_zip["expected_header_text"]
