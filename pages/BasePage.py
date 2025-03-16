import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Запрашиваем урл текущей страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.title('Ищем элемент (на странице)')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ищем много элементов')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.title('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Берем текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.title('Добавляем текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Функция перетаскивания элемента - drag and drop')
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        source = self.find_element_with_wait(source)
        target = self.find_element_with_wait(target)
        return  action.drag_and_drop(source, target).perform()