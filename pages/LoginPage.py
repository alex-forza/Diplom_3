import allure
from locators.login_page_locators import LoginPageLocators
from pages.BasePage import BasePage

class LoginPage(BasePage):
    @allure.step('Получаем текст названия формы входа')
    def wait_login_form(self):
        return self.get_text_from_element(LoginPageLocators.login)

    @allure.step('Заполняем форму входа. Нажимаем "Войти"')
    def fill_login_form(self, mail, password):
        self.add_text_to_element(LoginPageLocators.email_input, mail)
        self.add_text_to_element(LoginPageLocators.password_input, password)
        self.click_to_element(LoginPageLocators.enter_button)

    @allure.step('Кликаем по кнопке "Восстановить пароль"')
    def go_to_password_recovery(self):
        self.click_to_element(LoginPageLocators.password_recovery)