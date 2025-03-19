import allure
from locators.recovery_page_locators import RecoveryPageLocators
from pages.BasePage import BasePage

class RecoveryPasswordPage(BasePage):
    @allure.step('Заполняем почту и нажимаем "Восстановить"')
    def fill_email_recovery(self, email):
        self.add_text_to_element(RecoveryPageLocators.email_input, email)
        self.click_to_element(RecoveryPageLocators.recovery_button)

    @allure.step('В поле "Пароль" нажимаем на "глаз" и ищем активность элемента')
    def active_field_password(self):
        self.click_to_element(RecoveryPageLocators.eye_icon_button)
        self.find_element_with_wait(RecoveryPageLocators.mark_active_field)

    @allure.step('Проверка активности поля')
    def active_field_or_not(self):
        active = (self.find_element_with_wait(RecoveryPageLocators.mark_active_field)
                  != self.find_element_with_wait(RecoveryPageLocators.password_input))
        return active

    @allure.step('Проверка наличия текста "Восстановление пароля"')
    def is_text_recovery_password(self):
        return self.get_text_from_element(RecoveryPageLocators.recovery_form_forgot)

    @allure.step('Проверка наличия текста "Введите код из письма"')
    def is_text_code(self):
        return self.get_text_from_element(RecoveryPageLocators.code_input)