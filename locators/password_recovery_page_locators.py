from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//a[contains(text(),"Восстановить пароль")]'
    RECOVERY_BUTTON = By.XPATH, '//button[contains(text(),"Восстановить")]'
    EMAIL_INPUT = By.XPATH, '//input[@name="name"]'
    PASSWORD_RECOVERY_TEXT = By.XPATH, '//h2[contains(text(),"Восстановление пароля")]'
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[@class="input__icon input__icon-action"]'
    PASSWORD_INPUT_ACTIVE = By.XPATH, '//div[contains(@class, "input_status_active")]'