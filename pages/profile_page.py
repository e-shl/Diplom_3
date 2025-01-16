import allure

from locators.base_page_locators import *
from locators.profile_page_locators import *
from pages.base_page import BasePage


class ProfilePage (BasePage):

    @allure.step("Нажать кнопку Личный кабинет")
    def click_button_header_profile(self):
        self.find_clickable_element(BUTTON_LINK_PROFILE).click()
        self.wait_invisibility_element(LOADER_OVERLAY)

    @allure.step("Нажать кнопку Личный кабинет")
    def click_order_history(self):
        self.wait_invisibility_element(LOADER_OVERLAY)
        self.find_clickable_element(BUTTON_ORDER_HISTORY).click()

    @allure.step("Нажать кнопку Выйти")
    def click_logout_profile(self):
        self.wait_invisibility_element(LOADER_OVERLAY)
        self.find_clickable_element(BUTTON_LOGOUT_PROFILE).click()

    @allure.step("Ожидание окна Заказ создан - Ваш заказ начали готовить")
    def check_form_login(self):
        return self.find_clickable_element(FORM_LOGIN)

    @allure.step("Ожидание выбора Истории заказов")
    def check_selected_history(self):
        return self.find_clickable_element(SELECTED_BUTTON_ORDER_HISTORY)