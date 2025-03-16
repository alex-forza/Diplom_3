import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.BasePage import BasePage
from data import Urls

class ProfilePage(BasePage):
    @allure.step('Инициируем открытие страницы')
    def profile_page_url(self):
        return self.get_url(Urls.profile_url)

    @allure.step('Ждем кнопки "История заказов" и кликаем по ней')
    def click_history_button(self):
        self.find_element_with_wait(ProfilePageLocators.order_history)
        self.find_elements_with_wait(ProfilePageLocators.order_history)
        self.click_to_element(ProfilePageLocators.order_history)
        return self.get_url()