import pytest
import allure

from locators.login_page_locators import *
from pages.base_page import BasePage
from pages.login_page import LoginPage
from tests_data import TEST_EMAIL
from urls import *

@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title('Тест переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_button_open_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_link_forgot_password()
        assert login_page.find_clickable_element(BUTTON_FORGOT_PASSWORD)

    @allure.title('Тест ввод почты и клик по кнопке «Восстановить»')
    def test_button_open_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_forgot_password_page()
        login_page.send_email(TEST_EMAIL)
        login_page.click_link_forgot_password()
        assert login_page.find_clickable_element(BUTTON_SAVE) and login_page.get_current_url() == RESET_PASSWORD_PAGE_URL

    @allure.title('Тест ввод почты и клик по кнопке «Восстановить»')
    def test_button_open_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_forgot_password_page()
        login_page.send_email(TEST_EMAIL)
        login_page.click_link_forgot_password()
        login_page.find_clickable_element(BUTTON_SAVE)
        login_page.send_password(TEST_EMAIL)
        login_page.click_show_password()
        assert login_page.get_type_input(FILED_PASSWORD) == "text"