import pytest
import data
from helpers import WebDriverChoose

@pytest.fixture(params=['chrome','firefox'])
def driver(request):
    driver = WebDriverChoose.choose_browser(request.param)
    driver.get(data.Urls.url)
    driver.maximize_window()
    yield driver
    driver.quit()