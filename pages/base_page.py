import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить кликабельный элемент')
    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 200).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

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