from selenium.webdriver.common.by import By


class OrderListLocators:
    ORDER_LIST_TEXT = By.XPATH, '//h1[contains(text(),"Лента заказов")]'
    ORDER = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'
    CONSIST_TEXT = By.XPATH, '//p[text()="Cостав"]'
    ORDERS_LIST = By.XPATH, '//*[text()="#0{num_order}"]'
    ALL_TIME_ORDERS = (By.XPATH,
                       '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]')
    TODAY_ORDERS = (By.XPATH,
                    '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]')
    ORDERS_IN_WORK = By.XPATH, '//*[contains(@class, "orderListReady")]//li[contains(@class, "digits-default")]'
    ALL_ORDERS_READY = By.XPATH, '//li[@class="text text_type_main-small"]'