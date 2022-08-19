import pytest
from selenium import webdriver


@pytest.fixture()
def browser():


    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe", options=options)
    yield browser
    browser.quit()


@pytest.fixture()
def api():
    print("API test start")
    yield
    print("API test end")