from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    email_input = [By.XPATH, ".//label[text()='Email']"]
    name_input = [By.XPATH, ".//label[text()='Имя']"]
    password_input = [By.XPATH, ".//label[text()='Пароль']"]
    registration_form = [By.XPATH, ".//div/main/div/form"]
    already_registration = [By.XPATH, ".//p[text()='Уже зарегистрированы?']"]
    link_already_registration = [By.XPATH, ".//a[text()='Войти']"]