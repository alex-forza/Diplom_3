from selenium.webdriver.common.by import By

class LoginPageLocators:
    incorrect_password = [By.XPATH, ".//p[text()='Некорректный пароль']"]
    enter_button = [By.XPATH, ".//button[contains(text(),'Войти')]"]
    email_input = [By.XPATH, ".//input[@type='text']"]
    password_input = [By.XPATH, ".//input[@type='password']"]
    forgot_password = [By.XPATH, ".//p[text()='Забыли пароль?']"]
    password_recovery = [By.XPATH, ".//a[text()='Восстановить пароль']"]
    login = [By.XPATH, ".//h2[text()='Вход']"]
    eye_button = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]