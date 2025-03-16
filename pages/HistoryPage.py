import allure
from locators.history_page_locators import HistoryPageLocators
from pages.BasePage import BasePage
from data import Urls

class HistoryPage(BasePage):
    @allure.step('Открытие страницы заказов')
    def history_page_url(self):
        return self.get_url(Urls.history_url)

    @allure.step('Нажимаем кнопку выхода из личного кабинета')
    def click_logout(self):
        self.find_element_with_wait(HistoryPageLocators.logout_button).click()

    @allure.step('Нажимаем на последний сделанный заказ')
    def click_last_order(self):
        self.find_element_with_wait(HistoryPageLocators.last_order)
        self.click_to_element(HistoryPageLocators.last_order)

    @allure.step('Закрываем модальное окно заказа')
    def close_modal_window(self):
        self.find_element_with_wait(HistoryPageLocators.close_modal_window).click()

    @allure.step('Получаем номер последнего заказа')
    def get_last_order_number(self):
        return self.get_text_from_element(HistoryPageLocators.last_order_number)

    @allure.step('Нажимаем на ленту заказов в шапке')
    def go_feed_orders(self):
        self.find_element_with_wait(HistoryPageLocators.feed_orders).click()