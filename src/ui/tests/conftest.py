import logging
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.ui.enums.urls import URLS


@pytest.fixture(scope="session")
def logger() -> logging.Logger:
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


@pytest.fixture()
def driver(logger):
    logger.info("Running class setUp")

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(chrome_options)
    driver.implicitly_wait(10)
    driver.get(URLS.HOME_PAGE.value)
    driver.maximize_window()

    yield driver

    logger.info("Running class tearDown")
    driver.quit()
