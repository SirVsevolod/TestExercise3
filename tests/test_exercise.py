from pages.api import *
from pages.YandexPage import YandexPage
from pages.MainPage import MainPage


def test_get_requests(api):
    res = get_users()
    assert all(res), f'ERROR: {res}'


def test_post_requests(api):
    res = post_request()
    assert res, f"ERROR: {res}"


def test_search_link(browser):
    link = 'https://www.yandex.ru'
    page = YandexPage(browser, link)
    page.open()
    link = page.search("Planet for me")
    page = YandexPage(browser, link)
    assert page.cheak_links(), "ERROR: https://planetfor.me not found"


def test_search_qa(browser):
    link = 'https://planetforme.ru/'
    page = MainPage(browser, link)
    page.open()
    link = page.search("qa")
    page = MainPage(browser, link)
    assert page.cheak_news(), "ERROR: Новости не найдены"

