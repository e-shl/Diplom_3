import pytest
from selenium import webdriver

from locators.login_page_locators import *
from locators.profile_page_locators import *
from pages.designer_page import DesignerPage
from pages.login_page import LoginPage
from tests_data import *


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.send_email(BASE_EMAIL)
    login_page.send_password(BASE_PASSWORD)
    login_page.click_button_login()
    login_page.check_place_order()
    return driver

@pytest.fixture
def authorization_place_order(authorization):
    designer_page = DesignerPage(authorization)
    designer_page.create_order()
    return authorization