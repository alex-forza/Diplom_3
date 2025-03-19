import time
import allure
import helpers
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.ProfilePage import ProfilePage
from pages.FeedPage import AllOrdersPage

class TestProfilePage:
    @allure.title('Проверка успешной деавторизации после авторизации')
    @allure.description('ОР: в форме есть текст "Вход" (успешно деавторизовались)')
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.find_and_click_profile_link()
        name = helpers.name_generator()
        mail = helpers.mail_generator()
        password = helpers.password_generator()
        login_page.reg_rand_data(name, mail, password)

        main_page.find_and_click_profile_link()
        login_page.fill_login_form(mail,password)
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.find_and_click_profile_link()
        profile_page.click_logout_profile_page()
        assert 'Вход' in login_page.wait_login_form()

    @allure.title('Проверка перехода в личный кабинет после авторизации')
    @allure.description('ОР: отображается надпись "В этом разделе вы можете изменить свои перс.данные"')
    def test_pass_personal_account(self,driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        main_page.find_and_click_profile_link()
        name = helpers.name_generator()
        mail = helpers.mail_generator()
        password = helpers.password_generator()
        login_page.reg_rand_data(name, mail, password)

        main_page.find_and_click_profile_link()
        login_page.fill_login_form(mail,password)
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.find_and_click_profile_link()
        assert profile_page.get_text_from_button() == 'В этом разделе вы можете изменить свои персональные данные'

    @allure.title('Проверка перехода в историю заказов')
    @allure.description('ОР: отображается надпись "Выполнено за все время:"')
    def test_pass_history(self,driver):
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.click_feed_orders()
        assert feed_page.search_text_all_time() == 'Выполнено за все время:'