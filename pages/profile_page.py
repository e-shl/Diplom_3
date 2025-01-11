import allure

from locators.profile_page_locators import *
from pages.base_page import BasePage
from urls import *


class ProfilePage (BasePage):

    @allure.step("Нажать кнопку Личный кабинет")
    def click_button_header_profile(self):
        self.find_clickable_element(BUTTON_LINK_PROFILE).click()

    @allure.step("Нажать кнопку Личный кабинет")
    def click_order_history(self):
        self.find_clickable_element(BUTTON_ORDER_HISTORY).click()

    @allure.step("Нажать кнопку Выйти")
    def click_logout_profile(self):
        self.find_clickable_element(BUTTON_LOGOUT_PROFILE).click()