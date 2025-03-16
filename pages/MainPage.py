import allure
from locators.main_page_locators import MainPageLocators
from pages.BasePage import BasePage
from data import Urls

class MainPage(BasePage):
    @allure.step('Инициируем открытие страницы')
    def main_page_open(self):
        return self.driver.get(Urls.url)

    @allure.step('Ожидаем прогрузки')
    def wait_buns(self):
        self.find_elements_with_wait(MainPageLocators.buns_logo)
        self.find_element_with_wait(MainPageLocators.buns)

    @allure.step('Ищем и жмем "Личный кабинет"')
    def find_and_click_profile_link(self):
        self.find_element_with_wait(MainPageLocators.personal_account)
        self.click_to_element(MainPageLocators.personal_account)

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_create_order(self):
        self.find_element_with_wait(MainPageLocators.create_order)
        self.click_to_element(MainPageLocators.create_order)

    @allure.step('Берем номер заказа и сохраняем его для дальнейшего использования')
    def wait_order_modal_counter(self):
        self.find_element_with_wait(MainPageLocators.create_order_modal)
        return self.get_text_from_element(MainPageLocators.create_order_modal)

    @allure.step('Функция закрытия модального окна с номером созданного заказа')
    def close_order_modal_counter(self):
        self.click_to_element(MainPageLocators.close_order_modal)

    @allure.step('Жмем на карточку булки и получаем модальное окно с деталями ингредиента')
    def click_on_ingredients(self):
        self.find_element_with_wait(MainPageLocators.first_bun)
        self.click_to_element(MainPageLocators.first_bun)

    @allure.step('Получаем текст модального окна')
    def get_text_ingredients_module(self):
        self.find_element_with_wait(MainPageLocators.ingredient_active)
        self.find_element_with_wait(MainPageLocators.ingredient_details)
        self.get_text_from_element(MainPageLocators.ingredient_details)
        return self.get_text_from_element(MainPageLocators.ingredient_details)

    @allure.step('Закрываем модальное окно ингредиентов')
    def close_info_ingredients(self):
        self.find_element_with_wait(MainPageLocators.ingredient_close).click()

    @allure.step('Проверка закрытия модального окна с ингредиентами')
    def check_hide_info_ingredients_modal(self):
        self.find_element_with_wait(MainPageLocators.ingredient_hidden)

    @allure.step('Нажимаем на "Лента заказов"')
    def click_feed_orders(self):
        self.find_element_with_wait(MainPageLocators.feed_orders).click()

    @allure.step('Перетаскиваем булку в область конструктора')
    def drag_and_drop_element(self):
        return self.drag_and_drop(MainPageLocators.bun_drag, MainPageLocators.constructor_drop)

    @allure.step('Получаем текст счетчика ингредиента в списке ингредиентов')
    def get_counter_text(self):
        return self.get_text_from_element(MainPageLocators.counter)

    @allure.step ('Получаем текст блока "Булки"')
    def get_text_buns(self):
        return self.get_text_from_element(MainPageLocators.buns)