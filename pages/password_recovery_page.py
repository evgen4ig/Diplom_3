import allure
from pages.base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class PasswordRecoveryPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль')
    def click_password_recovery_button(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.move_to_element_and_click(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Клик на кнопку показать/скрыть пароль')
    def click_show_hide_password_button(self):
        self.click_element(PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Ввод данных в инпут "Email"')
    def send_data_to_email_input(self, data):
        self.send_input(PasswordRecoveryPageLocators.EMAIL_INPUT, data)

    @allure.step('Проверяем активность поля "Пароль"')
    def check_password_field_status(self):
        return self.find_element(PasswordRecoveryPageLocators.PASSWORD_INPUT_ACTIVE)

    @allure.step('Собираем текст с кнопки "Восстановить"')
    def get_text_from_recovery_button(self):
        return self.get_text(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Собираем текст с заголовка "Востановление Пароля"')
    def get_text_password_recovery(self):
        return self.get_text(PasswordRecoveryPageLocators.PASSWORD_RECOVERY_TEXT)