import allure
from selenium.webdriver import ActionChains

from locators.base_page_locators import *
from locators.order_feed_locators import *
from locators.profile_page_locators import *
from pages.base_page import BasePage


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
        ActionChains(self.driver).drag_and_drop(ingredient, order).pause(2).release(order).pause(2).perform()

    @allure.step("Нажать кнопку Оформить заказ")
    def click_place_order(self):
        self.find_clickable_element(BUTTON_PLACE_ORDER).click()

    @allure.step("Нажать кнопку Закрыть окно Заказ создан")
    def click_close_place_order(self):
        self.find_clickable_element(BUTTON_CLOSE_WINDOW_START_ORDER).click()

    @allure.step("Создание заказа")
    def create_order(self):
        self.open_base_page()
        self.move_ingredient_to_order()
        self.click_place_order()
        self.wait_invisibility_element(LOADER_START_ORDER)
        new_number_order = self.get_text(NUMBER_INFO_ORDER)
        self.click_close_place_order()
        return new_number_order
