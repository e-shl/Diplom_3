import pytest
import allure
from selenium.webdriver import ActionChains

from locators.base_page_locators import *
from locators.profile_page_locators import *
from pages.designer_page import DesignerPage
from tests_data import *
from urls import *

@allure.suite("Проверка основного функционала (Конструктор)")
class TestDesignerFunctional:

    @allure.title('Тест переход по клику на «Конструктор»')
    def test_click_button_header_designer_is_opened_designer_page(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_order_feed_page()
        designer_page.click_button_header_designer()
        assert designer_page.find_clickable_element(BUTTON_LOGIN_ACCOUNT) and designer_page.get_current_url() == BASE_URL + "/"

    @allure.title('Тест переход по клику на «Лента заказов»')
    def test_click_button_header_order_feed_is_opened_order_feed(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.click_button_header_order_feed()
        assert designer_page.find_clickable_element(LIST_ORDER_FEED) and designer_page.get_current_url() == ORDER_FEED_PAGE_URL

    @allure.title('Тест если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_is_opened_info_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.click_ingredient()
        assert designer_page.find_clickable_element(INFO_INGREDIENT)

    @allure.title('Тест всплывающее окно закрывается кликом по крестику')
    def test_click_close_info_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.click_ingredient()
        designer_page.find_clickable_element(INFO_INGREDIENT)
        designer_page.click_close_info_ingredient()
        assert designer_page.wait_invisibility_element(INFO_INGREDIENT)

    @allure.title('Тест при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_is_change_counter_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.move_ingredient_to_order()
        assert designer_page.find_clickable_element(COUNTER_INGREDIENT).text == "2"

    @allure.title('Тест залогиненный пользователь может оформить заказ')
    def test_logined_user_can_place_order(self, authorization):
        designer_page = DesignerPage(authorization)
        designer_page.open_base_page()
        designer_page.move_ingredient_to_order()
        designer_page.click_place_order()
        assert designer_page.find_clickable_element(WINDOW_START_ORDER)