from selenium.webdriver.common.by import By

# Номер созданого заказа в истории и ленте
NUMBERS_HISTORY_ORDER = (By.XPATH, '//*[contains(@class,"rderHistory_textBox__")]//*[contains(@class,"text_type_digits-default")]')
# Окно информации о заказе
INFO_ORDER = (By.XPATH, '//*[contains(@class,"odal_orderBox_")]')
# Количество Выполнено за всё время
ALL_TIME_ORDERS = (By.XPATH, '//*[contains(text(),"Выполнено за все время")]/..//*[contains(@class,"rderFeed_number__")]')
# Количество Выполнено за сегодня
DAY_ORDERS = (By.XPATH, '//*[contains(text(),"Выполнено за сегодня")]/..//*[contains(@class,"rderFeed_number__")]')
# Номер созданого заказа в окне информации о заказе
NUMBER_INFO_ORDER = (By.XPATH, '//*[contains(@class,"Modal_modal__title__")]')
# Все номера заказов в разделе В работе
ORDERS_IN_WORK = (By.XPATH, '//*[contains(@class,"OrderFeed_orderListReady_")]')
# Все текущие заказы готовы!
ALL_ORDERS_READY = (By.XPATH, '//*[contains(text(),"Все текущие заказы готовы!")]')