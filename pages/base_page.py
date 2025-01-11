import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import *
from urls import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть Главную страницу")
    def open_base_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Открыть страницу Войти")
    def open_login_page(self):
        self.driver.get(LOGIN_PAGE_URL)

    @allure.step("Открыть страницу Лента Заказов")
    def open_order_feed_page(self):
        self.driver.get(ORDER_FEED_PAGE_URL)

    @allure.step("Нажать кнопку Конструктор")
    def click_button_header_designer(self):
        self.find_clickable_element(BUTTON_HEADER_DESIGNER).click()

    @allure.step("Нажать кнопку Лента заказов")
    def click_button_header_order_feed(self):
        self.find_clickable_element(BUTTON_HEADER_ORDER_FEED).click()

    @allure.step("Открыть страницу Личный кабинет")
    def open_profile_page(self):
        self.driver.get(PROFILE_PAGE_URL)

    @allure.step('Получить кликабельный элемент')
    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 200).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получить кликабельный элемент')
    def find_all_elements(self, locator):
        self.find_clickable_element(locator)
        return self.driver.find_elements(*locator)

    @allure.step('Ждать исчезновения элемента')
    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Прокрутить к элементу')
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))

    @allure.step('Получить текста')
    def get_text(self, locator):
        text = self.find_clickable_element(locator).text
        return text

    @allure.step('Получить тип поля')
    def get_type_input(self, locator):
        text = self.find_clickable_element(locator).get_attribute("type")
        return text

    @allure.step('Перейти на другую вкладку')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url