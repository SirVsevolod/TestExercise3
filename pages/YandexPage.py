from .base_page import BasePage
from .locators import YandexLocators


class YandexPage(BasePage):
    def search(self, text):
        search = self.wait_visible(YandexLocators.INPUT_SEARCH)
        search.click()
        search.send_keys(text)
        button = self.wait_visible(YandexLocators.SEARCH_BUTTON)
        button.click()
        return self.browser.current_url


    def cheak_links(self):
        links = []
        elements = self.wait_elements(YandexLocators.LINKS)
        for element in elements:
            links.append(element.get_attribute('href'))
        return True if 'https://planetfor.me/' in links else False

