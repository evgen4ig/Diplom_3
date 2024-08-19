import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем браузер на заданом урле')
    def open(self, url):
        return self.driver.get(url)

    @allure.step('Собираем текущий урл')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Дожидаемся смены урла')
    def wait_url_change(self, url, time=15):
        return WebDriverWait(self.driver, time).until(ec.url_to_be(url))

    @allure.step('Дожаться пропажи элемента')
    def wait_element_disappear(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.invisibility_of_element(locator))

    @allure.step('Проверяем видимость элемента')
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator))

    @allure.step('Проверяем присутсвие элемента')
    def presence_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))

    @allure.step('Собираем текст с элемента')
    def get_text(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).text

    @allure.step('Ожидаем элемент и кликаем по нему')
    def click_element(self, locator, time=15):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Перемещаемся до элемента и кликаем')
    def move_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ac(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Ожидаем элемент и вводим данные')
    def send_input(self, locator, data, time=15):
        WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).send_keys(data)

    @allure.step('Перенос эллемента')
    def drag_and_drop(self, element, target):
        return ac(self.driver).drag_and_drop(element, target).perform()