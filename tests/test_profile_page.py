import allure

from locators.profile_page_locators import *
from pages.profile_page import ProfilePage
from urls import *

@allure.suite("Личный кабинет")
class TestProfilePage:

    @allure.title('Тест переход по клику на «Личный кабинет»')
    def test_link_profile_is_opened_profile_page(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.open_base_page()
        profile_page.click_button_header_profile()
        assert profile_page.find_clickable_element(FORM_LOGIN) and profile_page.get_current_url() == LOGIN_PAGE_URL

    @allure.title('Тест переход в раздел «История заказов»')
    def test_button_history_is_opened_order_history(self, authorization):
        profile_page = ProfilePage(authorization)
        profile_page.open_profile_page()
        profile_page.click_order_history()
        assert profile_page.find_clickable_element(SELECTED_BUTTON_ORDER_HISTORY) and profile_page.get_current_url() == ORDER_HISTORY_PROFILE_PAGE_URL

    @allure.title('Тест выход из аккаунта')
    def test_logout_profile_is_open_login_page(self, authorization):
        profile_page = ProfilePage(authorization)
        profile_page.open_profile_page()
        profile_page.click_logout_profile()
        assert profile_page.find_clickable_element(FORM_LOGIN) and profile_page.get_current_url() == LOGIN_PAGE_URL
