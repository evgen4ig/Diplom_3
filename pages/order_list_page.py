import allure

from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListLocators
from locators.profile_page_locators import ProfilePageLocators


class OrderList(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль')
    def click_password_recovery_button(self):
        self.move_to_element_and_click()

    @allure.step('Клик по заказу в листе заказов')
    def click_order(self):
        self.click_element(OrderListLocators.ORDER)

    @allure.step('Поиск элемента по номеру заказа')
    def search_element_by_order_number(self, num_order):
        str_num_order = OrderListLocators.ORDERS_LIST
        str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
        return self.find_element(str_num_order)

    @allure.step('Собираем количество заказов за все время')
    def get_all_time_counter(self):
        return self.get_text(OrderListLocators.ALL_TIME_ORDERS)

    @allure.step('Собираем количество заказов за сегодня')
    def get_today_counter(self):
        return self.get_text(OrderListLocators.TODAY_ORDERS)

    @allure.step('Собираем номер заказа в работе')
    def get_in_work_order_number(self):
        return self.get_text(OrderListLocators.ORDERS_IN_WORK)

    @allure.step('Собираем текст с окна состава')
    def get_text_from_consist(self):
        return self.get_text(OrderListLocators.CONSIST_TEXT)

    @allure.step('Собираем текст с номера заказа')
    def get_text_from_order_number(self):
        return self.get_text(ProfilePageLocators.ORDER_NUMBER)