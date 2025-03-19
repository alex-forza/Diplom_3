from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    email_input = [By.XPATH, "(.//input[@type='text'])[2]"]
    name_input = [By.XPATH, "(.//input[@type='text'])[1]"]
    password_input = [By.XPATH, ".//input[@type='password']"]
    registration_form = [By.XPATH, ".//div/main/div/form"]
    already_registration = [By.XPATH, ".//p[text()='Уже зарегистрированы?']"]
    link_already_registration = [By.XPATH, ".//a[text()='Войти']"]
    registration_button = [By.XPATH, ".//a[@class='Auth_link__1fOlj' and @href='/register']"]
    complete_registration = [By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]