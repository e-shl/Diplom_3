import allure

from locators.base_page_locators import *
from locators.login_page_locators import *
from locators.profile_page_locators import BUTTON_LOGIN, BUTTON_PLACE_ORDER
from pages.base_page import BasePage
from urls import *


class LoginPage (BasePage):

    @allure.step("Нажать ссылку Восстановить пароль")
    def click_link_forgot_password(self):
        self.find_clickable_element(BUTTON_LINK_FORGOT_PASSWORD).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Заполнить поле Email")
    def send_email(self, email):
        self.find_clickable_element(FILED_EMAIL).send_keys(email)

    @allure.step("Нажать кнопку Восстановить")
    def click_button_forgot_password(self):
        self.find_clickable_element(BUTTON_FORGOT_PASSWORD).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Ожидать кнопку Восстановить")
    def check_button_forgot_password(self):
        return self.find_clickable_element(BUTTON_FORGOT_PASSWORD)

    @allure.step("Заполнить поле Пароль")
    def send_password(self, password):
        self.find_clickable_element(FILED_PASSWORD).send_keys(password)

    @allure.step("Нажать кнопку Глаз (показать пароль)")
    def click_show_password(self):
        self.find_clickable_element(SHOW_PASSWORD).click()

    @allure.step("Нажать кнопку Войти")
    def click_button_login(self):
        self.find_clickable_element(BUTTON_LOGIN).click()

    @allure.step("Ожидание кнопки Оформить заказ")
    def check_place_order(self):
        return self.find_clickable_element(BUTTON_PLACE_ORDER)

    @allure.step("Ожидание кнопки Оформить заказ")
    def check_button_save(self):
        return self.find_clickable_element(BUTTON_SAVE)
