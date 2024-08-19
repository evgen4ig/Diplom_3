from selenium.webdriver.common.by import By


class ProfilePageLocators:
    EMAIL_INPUT = By.XPATH, '//input[@name="name"]'
    PASSWORD_INPUT = By.XPATH, '//input[@name="Пароль"]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(),"Войти")]'
    ORDER_HISTORY_BUTTON = By.XPATH, '//a[contains(text(),"История заказов")]'
    LOGOUT_BUTTON = By.XPATH, '//button[contains(text(),"Выход")]'
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'