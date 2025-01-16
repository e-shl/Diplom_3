import allure

from locators.order_feed_locators import *
from pages.designer_page import DesignerPage
from pages.order_feed_page import OrderFeedPage

@allure.suite("Проверка основного функционала (Конструктор)")
class TestOrderFeed:

    @allure.title('Тест после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_have_in_work(self, authorization):
        order_feed_page = DesignerPage(authorization)
        new_number_order = order_feed_page.create_order()
        order_feed_page.click_button_header_order_feed()
        order_feed_page.wait_invisibility_element(ALL_ORDERS_READY)
        assert new_number_order in order_feed_page.get_text(ORDERS_IN_WORK)

    @allure.title('Тест если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_is_opened_order_info(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        order_feed_page.click_order_in_history()
        assert order_feed_page.check_window_info_order()

    @allure.title('Тест заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_history_have_too_feed(self, authorization_place_order):
        order_feed_page = OrderFeedPage(authorization_place_order)
        order_feed_page.open_profile_page()
        order_feed_page.click_order_history()
        order_from_history = order_feed_page.get_last_order_history()
        order_feed_page.open_order_feed_page()
        assert order_feed_page.get_check_number_order(order_from_history)

    @allure.title('Тест при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_change_all_time_order(self, authorization):
        order_feed_page = DesignerPage(authorization)
        order_feed_page.open_order_feed_page()
        old_all_time_order = order_feed_page.get_text(ALL_TIME_ORDERS)
        order_feed_page.create_order()
        order_feed_page.open_order_feed_page()
        new_all_time_order = order_feed_page.get_text(ALL_TIME_ORDERS)
        assert new_all_time_order > old_all_time_order

    @allure.title('Тест при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_change_day_time_order(self, authorization):
        order_feed_page = DesignerPage(authorization)
        order_feed_page.open_order_feed_page()
        old_day_time_order = order_feed_page.get_text(DAY_ORDERS)
        order_feed_page.create_order()
        order_feed_page.open_order_feed_page()
        new_day_time_order = order_feed_page.get_text(DAY_ORDERS)
        assert new_day_time_order > old_day_time_order
