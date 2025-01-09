import allure

from locators.login_page_locators import *
from pages.base_page import BasePage
from urls import *


class LoginPage (BasePage):

    @allure.step("Открыть страницу Войти")
    def open_login_page(self):
        self.driver.get(LOGIN_PAGE_URL)

    @allure.step("Нажать ссылку Восстановить пароль")
    def click_link_forgot_password(self):
        self.find_clickable_element(BUTTON_LINK_FORGOT_PASSWORD).click()

    @allure.step("Открыть страницу Восстановление пароля")
    def open_forgot_password_page(self):
        self.driver.get(FORGOT_PASSWORD_PAGE_URL)

    @allure.step("Заполнить поле Email")
    def send_email(self, email):
        self.find_clickable_element(FILED_EMAIL).send_keys(email)

    @allure.step("Нажать кнопку Восстановить")
    def click_link_forgot_password(self):
        self.find_clickable_element(BUTTON_FORGOT_PASSWORD).click()

    @allure.step("Заполнить поле Пароль")
    def send_password(self, email):
        self.find_clickable_element(FILED_PASSWORD).send_keys(email)

    @allure.step("Нажать кнопку Глаз (показать пароль)")
    def click_show_password(self):
        self.find_clickable_element(SHOW_PASSWORD).click()