from selenium.webdriver.chrome.webdriver import WebDriver

from ui.pages.home_page import HomePage


# TODO rename the test
def test_positive_first(driver: WebDriver, logger):
    zip_code = 10001
    # name = 'Johan Frame'
    # email = 'j.frame@gmail.com'
    # phone_number = 1234567890

    home_page: HomePage = HomePage(driver, logger)

    logger.info(f'Fill zip_code {zip_code} and start estimation')
    home_page.fill_zip_code(zip_code)
    home_page.submit_zip_code()
    assert driver.current_url == 'https://hb-autotests.stage.sirenltd.dev/hvac'
