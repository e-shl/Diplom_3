import allure

from locators.order_feed_locators import *
from locators.profile_page_locators import *
from pages.base_page import BasePage


class OrderFeedPage (BasePage):

    @allure.step("Нажать ссылку Восстановить пароль")
    def click_order_in_history(self):
        self.find_clickable_element(NUMBERS_HISTORY_ORDER).click()

    @allure.step("Нажать кнопку Личный кабинет")
    def click_order_history(self):
        self.find_clickable_element(BUTTON_ORDER_HISTORY).click()

    @allure.step("Получить номер последнего заказа из История заказов")
    def get_last_order_history(self):
        return self.find_all_elements(NUMBERS_HISTORY_ORDER)[-1].text

    @allure.step("Проверить существование последнего номера заказа в Ленте заказов")
    def get_check_number_order(self, last_order):
        return self.find_clickable_element((By.XPATH, f'//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default") and contains(text(),"{last_order}")]'))