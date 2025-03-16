import allure
from data import StaticData
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.HistoryPage import HistoryPage
from pages.ProfilePage import ProfilePage

class TestProfilePage:
    @allure.title('Логинимся -> переходим в личный кабинет -> переходим в историю заказов ->'
                  '-> выходим из аккаунта -> проверяем успешность деавторизации')
    @allure.description('ОР: в форме есть текст "Вход" (успешно деавторизовались)')
    def test_login_history_logout(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        history_page = HistoryPage(driver)
        main_page.find_and_click_profile_link()
        login_page.fill_login_form(StaticData.static_user_email, StaticData.static_user_password)
        main_page.find_and_click_profile_link()
        profile_page.click_history_button()
        history_page.click_logout()
        assert 'Вход' in login_page.wait_login_form()