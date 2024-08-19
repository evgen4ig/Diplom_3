import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListLocators


class MainPage(BasePage):
    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_order_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.step('Клик по ингридиенту')
    def click_ingredient_button(self):
        self.move_to_element_and_click(MainPageLocators.INGREDIENT)

    @allure.step('Клик по кнопке закрытия')
    def click_close_popup_window_button(self):
        self.move_to_element_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверить наличие элемента на экране')
    def check_ingredients_details_on_screen(self):
        return self.presence_element(MainPageLocators.INGREDIENT_DETAILS_TEXT).is_displayed()

    @allure.step('Дождаться исчезновения деталей заказа')
    def wait_for_order_details_disappear(self):
        self.wait_element_disappear(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Кликнуть по кнопке "Оформить заказ')
    def click_order_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step('Добавить ингридиент в констуктор')
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(self.find_element(MainPageLocators.INGREDIENT),
                           self.find_element(MainPageLocators.BURGER_CONSTRUCTOR))

    @allure.step('Ищем нормер заказа во всплывающем окне')
    def find_order_number(self):
        self.find_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('Собираем текст с кнопки логин')
    def get_text_from_login_button(self):
        return self.get_text(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Собираем текст с листа заказов')
    def get_text_from_order_list(self):
        return self.get_text(OrderListLocators.ORDER_LIST_TEXT)

    @allure.step('Собираем текст с окна ингридиентов')
    def get_text_from_ingredients_details(self):
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step('Собираем текст со счетчика ингридиентов')
    def get_text_from_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Собираем текст с заказа')
    def get_text_from_order(self):
        return self.get_text(MainPageLocators.ORDER_TEXT)