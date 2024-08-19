import allure
from data import Url
from pages.profile_page import ProfilePage
from conftest import *

@allure.story('Проверка личного кабинета')
class TestProfilePage:
    @allure.title('Проверка перехода по кнопке "Личный кабинет"')
    def test_transition_to_profile_page(self, driver):
        page = ProfilePage(driver)
        page.open(Url.BASE_PAGE)
        page.click_lk_button()
        page.wait_url_change(Url.LOGIN_PAGE)
        assert (page.get_url() == Url.LOGIN_PAGE and
                page.get_text_password_recovery_button() == 'Восстановить пароль')

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_transition_to_order_history(self, driver, user):
        page = ProfilePage(driver)
        page.open(Url.LOGIN_PAGE)
        page.login(user)
        page.wait_url_change(Url.BASE_PAGE)
        page.click_lk_button()
        page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        page.click_order_history_button()
        assert page.get_url() == Url.ORDER_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта')
    def test_logaut(self, driver, user):
        page = ProfilePage(driver)
        page.open(Url.LOGIN_PAGE)
        page.login(user)
        page.wait_url_change(Url.BASE_PAGE)
        page.click_lk_button()
        page.wait_url_change(Url.ACCOUNT_PROFILE_PAGE)
        page.click_logout_button()
        assert (page.get_text_login_button() == 'Войти'
                and page.get_url() == Url.LOGIN_PAGE)