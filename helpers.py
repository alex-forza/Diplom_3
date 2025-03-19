import random
from selenium import webdriver

class WebDriverChoose:
    @staticmethod
    def choose_browser(name):
        if name == 'chrome':
            return webdriver.Chrome()
        elif name == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError(f'Недопустимый браузер: {name}')

def mail_generator():
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    name = ''.join(random.choice(letters) for i in range(10))
    domain = ''.join(random.choice(letters) for i in range(6))
    country = ['ru', 'com']
    mail = f'{name}@{domain}.{random.choice(country)}'
    return mail

def password_generator():
    symbols = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    password = ''.join(random.choice(symbols) for i in range(0, 10))
    return password

def name_generator():
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    first_name = ''.join(random.choice(letters) for i in range(10))
    last_name = ''.join(random.choice(letters) for i in range(10))
    return f"{first_name} {last_name}"