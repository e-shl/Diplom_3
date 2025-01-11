from selenium.webdriver.common.by import By

# Кнопка Конструктор
BUTTON_HEADER_DESIGNER = (By.XPATH, '//*[contains(text(),"Конструктор")]')
# Кнопка Войти в аккаунт
BUTTON_LOGIN_ACCOUNT = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
# Кнопка Лента заказов
BUTTON_HEADER_ORDER_FEED = (By.XPATH, '//a[@href="/feed"]')
# Список ленты заказов
LIST_ORDER_FEED = (By.XPATH, '//*[contains(@class,"OrderFeed_list__")]')
# Детали ингредиента
INFO_INGREDIENT = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')
# Ингредиент - Счётчик ингредиента
COUNTER_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]//*[contains(@class,"counter_default__")]')
# Кнопка Закрыть - Детали ингредиента
BUTTON_CLOSE_INFO_INGREDIENT  = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]/..//..//button[contains(@class,"Modal_modal__close")]')
# Простарнство сбора заказа (Перетяните булочку сюда (верх))
SPACE_ORDER = (By.XPATH, '(//*[contains(@class,"constructor-element__text")])[1]')
# Заказ создан - Ваш заказ начали готовить
WINDOW_START_ORDER = (By.XPATH, '//*[contains(text(),"Ваш заказ начали готовить")]')
# Кнопка Заказ создан - Ваш заказ начали готовить
BUTTON_CLOSE_WINDOW_START_ORDER = (By.XPATH, '//*[contains(text(),"Ваш заказ начали готовить")]/..//..//..//button[contains(@class,"Modal_modal__close")]')
# Процесс создания заказа - мешает взаимодействию с сайтом
LOADER_START_ORDER = (By.XPATH, '//div[contains(@class,"Modal_modal_opened__")]')