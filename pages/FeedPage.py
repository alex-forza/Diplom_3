import allure
from locators.feed_page_locators import FeedPageLocators
from pages.BasePage import BasePage
from data import Urls

class AllOrdersPage(BasePage):
    @allure.step('Открываем страницу')
    def feed_page_open(self):
        return self.get_url(Urls.feed_url)

    @allure.step('Берем текст счетчика за все время')
    def find_total_counter(self):
        self.find_element_with_wait(FeedPageLocators.all_time_count)
        return self.get_text_from_element(FeedPageLocators.all_time_count)

    @allure.step('Берем текст счетчика за сегодня')
    def find_today_counter(self):
        self.find_element_with_wait(FeedPageLocators.today_count)
        return self.get_text_from_element(FeedPageLocators.today_count)

    @allure.step('Получаем значение из раздела "В работе"')
    def order_in_progress(self):
        self.find_element_with_wait(FeedPageLocators.in_process_counter)
        return self.get_text_from_element(FeedPageLocators.in_process_counter)

    @allure.step('Щелкаем на иконку "Конструктор"')
    def click_to_constructor_icon(self):
        self.find_element_with_wait(FeedPageLocators.icon_constructor).click()

    @allure.step('Кликаем на первый заказ в списке и открываем его состав')
    def click_first_in_feed_orders(self):
        self.find_element_with_wait(FeedPageLocators.first_order).click()
        self.find_element_with_wait(FeedPageLocators.composition)
        return self.get_text_from_element(FeedPageLocators.composition)

    @allure.step('Поиск заказа пользователя в ленте')
    def search_user_order(self):
        self.find_elements_with_wait(FeedPageLocators.search_order)
        return self.get_text_from_element(FeedPageLocators.search_order)

    @allure.step('Ищем и возвращаем текст "Выполнено за все время"')
    def search_text_all_time(self):
        self.find_element_with_wait(FeedPageLocators.all_time_text)
        return self.get_text_from_element(FeedPageLocators.all_time_text)