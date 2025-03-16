import pytest
from selenium import webdriver
import data

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(data.Urls.url)
    driver.maximize_window()
    yield driver
    driver.quit()