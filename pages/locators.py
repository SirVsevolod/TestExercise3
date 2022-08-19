from selenium.webdriver.common.by import By


class YandexLocators():
    INPUT_SEARCH = (By.CSS_SELECTOR, 'input[class = "input__control input__input mini-suggest__input"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[class = "button mini-suggest__button button_theme_search button_size_search i-bem button_js_inited"]')
    LINKS = (By.CSS_SELECTOR, 'a[class="Link Link_theme_normal OrganicTitle-Link organic__url link"]')


class MainLocators():
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div[id="header-sticky-wrapper"] div[class="top-misc"] a[class="toggle-search-box"]')
    INFORMATION_TEXT = (By.CSS_SELECTOR, 'div[class="post-header"]  h1')
    SEARCH_SITKA = (By.CSS_SELECTOR, 'div[id="sitka-search-overlay"] input')
