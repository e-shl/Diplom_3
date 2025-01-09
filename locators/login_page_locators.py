from selenium.webdriver.common.by import By

BUTTON_LINK_FORGOT_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')
BUTTON_FORGOT_PASSWORD = (By.XPATH, '//button[text()="Восстановить"]')
FILED_EMAIL = (By.XPATH, '//*[contains(text(),"Email")]/parent::*/input')
BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]')
FILED_PASSWORD = (By.XPATH, '//*[contains(text(),"Пароль")]/parent::*/input')
SHOW_PASSWORD = (By.CLASS_NAME, 'input__icon-action')