from selenium.webdriver.common.by import By

class HistoryPageLocators:
    logout_button = [By.XPATH, ".//button[text()='Выход']"]
    history_orders = [By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']"]
    feed_orders = [By.XPATH, ".//p[text()='Лента Заказов']"]
    last_order = [By.XPATH, ".//div/div/ul/li[last()]"]
    last_order_number = [By.XPATH, ".//div/div/ul/li[last()]//p"]
    close_modal_window = [By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]