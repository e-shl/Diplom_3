import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_page_locators import *
from locators.profile_page_locators import *
from pages.login_page import LoginPage
from tests_data import *
from urls import LOGIN_PAGE_URL


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.find_clickable_element(FILED_EMAIL).send_keys(BASE_EMAIL)
    login_page.find_clickable_element(FILED_PASSWORD).send_keys(BASE_PASSWORD)
    login_page.find_clickable_element(BUTTON_LOGIN).click()
    login_page.find_clickable_element(BUTTON_PLACE_ORDER)
    yield driver
    driver.quit()