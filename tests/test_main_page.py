import allure
from pages.FeedPage import AllOrdersPage
from pages.HistoryPage import HistoryPage
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
from pages.ProfilePage import ProfilePage
import time
import helpers

class TestMainPage:
    @allure.title('Регистрируемся -> логинимся -> создаем заказ -> проверяем его в личном кабинете ->'
                  '-> проверяем его в ленте заказов')
    @allure.description('ОР: номер заказа в личном кабинете и лента соответствуют созданному номеру заказа')
    def test_order_from_history_exist_in_feed_orders(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        profile_page = ProfilePage(driver)
        history_page = HistoryPage(driver)

        main_page.find_and_click_profile_link()
        name = helpers.name_generator()
        mail = helpers.mail_generator()
        password = helpers.password_generator()
        login_page.reg_rand_data(name, mail, password)

        main_page.find_and_click_profile_link()
        login_page.fill_login_form(mail, password)
        main_page.drag_and_drop_element()
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.click_create_order()
        time.sleep(3) # топорная задержка для пересчета значения счетчика
        get_order_number = main_page.wait_order_modal_counter()
        main_page.close_order_modal_counter()
        main_page.find_and_click_profile_link()
        profile_page.click_history_button()
        history_page.click_last_order()
        history_page.get_last_order_number()
        time.sleep(1) #топорка, без которой в firefox не проходит/проходит через раз
        assert get_order_number in history_page.get_last_order_number()
        history_page.close_modal_window()
        history_page.go_feed_orders()
        time.sleep(1) #топорка, без которой в firefox не проходит/проходит через раз
        assert get_order_number in feed_page.search_user_order()

    @allure.title('Переходим с главной страницы в ленту заказов и обратно по кнопке конструктора')
    @allure.description('ОР: текст "булки" на главном экране')
    def test_from_constructor_to_feed_and_back(self, driver):
        main_page = MainPage(driver)
        feed_page = AllOrdersPage(driver)
        main_page.click_feed_orders()
        feed_page.click_to_constructor_icon()
        assert 'Булки' in main_page.get_text_buns()

    @allure.title('Нажимаем на булку на главной странице -> '
                  '-> открывается модальное окно -> закрываем модальное окно крестиком')
    @allure.description('ОР: модальное окно с текстом "Детали ингредиента", модальное окно закрывается по клику')
    def test_ingredient_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.wait_buns()
        main_page.click_on_ingredients()
        assert "Детали ингредиента" in main_page.get_text_ingredients_module()
        assert main_page.close_info_ingredients() != main_page.check_hide_info_ingredients_modal

    @allure.title('Перетаскиваем булку в конструктор методом drag and drop. Увеличение каунтера ингредиента')
    @allure.description('ОР: значение (счетчик) = 2')
    def test_add_ingredient_drag_and_drop(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_element()
        assert '2' in main_page.get_counter_text()

    @allure.title('Регистрируемся -> логинимся -> добавляем булку в конструктор ->'
                  '-> оформляем два заказа -> сравниваем их друг с другом (проверка счетчиков)')
    @allure.description('ОР: отсутствует отображение заглушки в виде числа 9999'
                        'и номер второго заказа больше номера первого')
    def test_login_and_create_orders(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        main_page.find_and_click_profile_link()
        name = helpers.name_generator()
        mail = helpers.mail_generator()
        password = helpers.password_generator()
        login_page.reg_rand_data(name, mail, password)

        main_page.find_and_click_profile_link()
        login_page.fill_login_form(mail,password)
        main_page.drag_and_drop_element()
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.click_create_order()
        time.sleep(3) #топорная задержка для пересчета значения счетчика
        data_1 = main_page.wait_order_modal_counter()
        assert data_1 != '9999' #проверка, что не отображается 'заглушка'
        main_page.close_order_modal_counter()
        main_page.drag_and_drop_element()
        main_page.click_create_order()
        time.sleep(3) #топорная задержка для пересчета значения счетчика
        data_2 = main_page.wait_order_modal_counter()
        assert data_1 < data_2

    @allure.title('Регистрируемся -> логинимся -> создаем заказ -> идем в ленту заказов -> ищем его в работе -> '
                  '-> нажимаем на первый заказ из списка')
    @allure.description('ОР: номер нашего заказа в работе, '
                        'при открытии первого заказа списка открывается модальное окно с текстом "Состав"')
    def test_check_feed_number(self, driver):
        login_page = LoginPage(driver)
        feed_page = AllOrdersPage(driver)
        main_page = MainPage(driver)

        main_page.find_and_click_profile_link()
        name = helpers.name_generator()
        mail = helpers.mail_generator()
        password = helpers.password_generator()
        login_page.reg_rand_data(name, mail, password)

        main_page.find_and_click_profile_link()
        login_page.fill_login_form(mail,password)
        main_page.drag_and_drop_element()
        time.sleep(1) # топорка, без которой в firefox не проходит
        main_page.click_create_order()
        time.sleep(3) #топорная задержка для пересчета значения счетчика
        get_order_num = main_page.wait_order_modal_counter()
        main_page.close_order_modal_counter()
        main_page.click_feed_orders()
        assert get_order_num in feed_page.order_in_progress()
        assert "Cостав" in feed_page.click_first_in_feed_orders()

    @allure.title('Регистрируемся -> логинимся -> переходим в ленту заказов -> '
                  '-> сохраняем счетчики -> создаём заказ -> сверяем счетчики')
    @allure.description('ОР: оба счетчика увеличили свои значения')
    def test_check_change_counters(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        main_page.find_and_click_profile_link()
        name = helpers.name_generator()
        mail = helpers.mail_generator()
        password = helpers.password_generator()
        login_page.reg_rand_data(name, mail, password)

        main_page.find_and_click_profile_link()
        login_page.fill_login_form(mail,password)
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.click_feed_orders()
        feed_page = AllOrdersPage(driver)
        total_counter = feed_page.find_total_counter()
        today_counter = feed_page.find_today_counter()
        main_page.main_page_open()
        main_page.drag_and_drop_element()
        time.sleep(1) #топорка, без которой в firefox не проходит
        main_page.click_create_order()
        time.sleep(3)  # топорная задержка для пересчета значения счетчика
        main_page.close_order_modal_counter()
        main_page.click_feed_orders()
        total_counter_new = feed_page.find_total_counter()
        today_counter_new = feed_page.find_today_counter()
        assert total_counter_new > total_counter
        assert today_counter_new > today_counter