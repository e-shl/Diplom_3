import allure

from locators.base_page_locators import *
from locators.login_page_locators import *
from pages.login_page import LoginPage
from tests_data import *
from urls import *

@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title('Тест переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_button_open_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_invisibility_element(LOADER_OVERLAY)
        login_page.click_link_forgot_password()
        assert login_page.check_button_forgot_password()

    @allure.title('Тест ввод почты и клик по кнопке «Восстановить»')
    def test_send_email_open_reset_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_forgot_password_page()
        login_page.send_email(BASE_EMAIL)
        login_page.click_button_forgot_password()
        assert login_page.check_button_save() and login_page.get_current_url() == RESET_PASSWORD_PAGE_URL

    @allure.title('Тест клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_button_show_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_forgot_password_page()
        login_page.send_email(BASE_EMAIL)
        login_page.click_button_forgot_password()
        login_page.check_button_save()
        login_page.send_password(BASE_EMAIL)
        login_page.click_show_password()
        assert login_page.get_type_input(FILED_PASSWORD) == "text"