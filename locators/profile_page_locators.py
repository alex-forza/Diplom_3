from selenium.webdriver.common.by import By

class ProfilePageLocators:
    save_button = [By.XPATH, ".//button[text()='Сохранить']"]
    logout_button = [By.XPATH, ".//button[text()='Выход']"]
    order_history = [By.XPATH, ".//a[text()='История заказов']"]