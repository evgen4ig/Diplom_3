from selenium.webdriver.common.by import By


class MainPageLocators:
    LK_BUTTON = By.XPATH, '//p[contains(text(),"Личный Кабинет")]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[contains(text(),"Конструктор")]'
    ORDER_LIST_BUTTON = By.XPATH, '//p[contains(text(),"Лента Заказов")]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(),"Войти в аккаунт")]'
    INGREDIENT = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'
    INGREDIENT_DETAILS_TEXT = By.XPATH, '//h2[contains(text(),"Детали ингредиента")]'
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'
    BURGER_CONSTRUCTOR = By.XPATH, '//*[@class="BurgerConstructor_basket__list__l9dp_"]'
    TOPPINGS_BUTTON = By.XPATH, '//span[contains(text(),"Начинки")]'
    INGREDIENT_COUNTER = (By.XPATH,
                          '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]')
    ORDER_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]'
    ORDER_TEXT = By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]'
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]'