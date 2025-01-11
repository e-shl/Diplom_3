import allure
from selenium.webdriver import ActionChains

from locators.base_page_locators import *
from locators.profile_page_locators import *
from pages.base_page import BasePage
from urls import *


class DesignerPage (BasePage):

    @allure.step("Нажать на ингридиент")
    def click_ingredient(self):
        self.find_clickable_element(COUNTER_INGREDIENT).click()

    @allure.step("Нажать на ингридиент")
    def click_close_info_ingredient(self):
        self.find_clickable_element(BUTTON_CLOSE_INFO_INGREDIENT).click()

    @allure.step("Перенос ингридиента в Заказ")
    def move_ingredient_to_order(self):
        ingredient = self.find_clickable_element(COUNTER_INGREDIENT)
        order = self.find_clickable_element(SPACE_ORDER)
        ActionChains(self.driver).drag_and_drop(ingredient, order).release(order).perform()

    @allure.step("Нажать кнопку Оформить заказ")
    def click_place_order(self):
        self.find_clickable_element(BUTTON_PLACE_ORDER).click()