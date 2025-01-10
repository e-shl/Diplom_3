from selenium.webdriver.common.by import By

# Ссылка/Кнопка Восстановить пароль
BUTTON_LINK_FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')
# Кнопка Восстановить
BUTTON_FORGOT_PASSWORD = (By.XPATH, '//button[text()="Восстановить"]')\
# Поле Email
FILED_EMAIL = (By.XPATH, '//*[contains(text(),"Email")]/parent::*/input')
# Кнопка Сохранить
BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]')
# Поле Пароль
FILED_PASSWORD = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')
# Кнопка Показать пароль
SHOW_PASSWORD = (By.CLASS_NAME, 'input__icon-action')