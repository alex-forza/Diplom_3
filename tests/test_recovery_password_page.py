import allure
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.RecoveryPage import RecoveryPasswordPage
from helpers import mail_generator

class TestRecoveryPassword:
    @allure.title('Проверка перехода в форму восстановления пароля, ввод почты и клик по кнопке "Восстановить",'
                  'активность кнопки скрытия пароля при её нажатии')
    @allure.description('ОР: текст "Восстановление пароля" по кнопке восстановления пароля, '
                        'текст "Введите код из письма", поле скрытия пароля активно при нажатии')
    def test_recovery_password_from_login_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPasswordPage(driver)
        main_page = MainPage(driver)
        main_page.find_and_click_profile_link()
        login_page.go_to_password_recovery()
        assert "Восстановление пароля" == recovery_page.is_text_recovery_password()
        recovery_page.fill_email_recovery(mail_generator())
        assert "Введите код из письма" == recovery_page.is_text_code()
        active_field = recovery_page.active_field_password()
        assert active_field != recovery_page.active_field_or_not