from .base_page import BasePage
from .locators import MainLocators
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def search(self, text):
        button = self.wait_visible(MainLocators.SEARCH_BUTTON)
        button.click()
        sitka = self.wait_visible(MainLocators.SEARCH_SITKA)
        sitka.send_keys(text)
        sitka.send_keys(Keys.ENTER)
        return self.browser.current_url

    def cheak_news(self):
        return self.wait_visible(MainLocators.INFORMATION_TEXT).text == "Nothing Found"

