import allure
from data import Url
from pages.password_recovery_page import PasswordRecoveryPage
from conftest import *

@allure.story('Проверки восстановления пароля')
class TestsPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_to_pass_recovery_page_by_button(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open(Url.LOGIN_PAGE)
        page.click_password_recovery_button()
        assert (page.get_url() == Url.FORGOT_PASSWORD_PAGE and
                page.get_text_from_recovery_button()) == 'Восстановить'

    @allure.title('Проверка клика по кнопке "Восстановить" с введеной существующей почтой')
    def test_enter_email_click_recovery(self, driver, user):
        page = PasswordRecoveryPage(driver)
        page.open(Url.FORGOT_PASSWORD_PAGE)
        page.send_data_to_email_input(user['email'])
        page.click_recovery_button()
        page.wait_url_change(Url.RESET_PASSWORD_PAGE)
        assert (page.get_url() == Url.RESET_PASSWORD_PAGE and
                page.get_text_password_recovery() == 'Восстановление пароля')

    @allure.title('Проверка кнопки показать/скрыть пароль')
    def test_show_hide_password_button(self, driver, user):
        page = PasswordRecoveryPage(driver)
        page.open(Url.FORGOT_PASSWORD_PAGE)
        page.send_data_to_email_input(user['email'])
        page.click_recovery_button()
        page.click_show_hide_password_button()
        assert page.check_password_field_status()