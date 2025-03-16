from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    email_input = [By.XPATH, ".//input[@type='text']"]
    recovery_button = [By.XPATH, ".//button[text()='Восстановить']"]
    eye_icon_button = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]
    password_input = [By.XPATH, ".//input[@type='password']"]
    recovery_form_forgot = [By.XPATH, ".//h2[text()='Восстановление пароля']"]
    mark_active_field = [By.XPATH,  ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']"]
    code_input = [By.XPATH, './/label[text()="Введите код из письма"]']