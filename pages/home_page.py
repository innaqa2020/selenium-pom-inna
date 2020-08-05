"""
This module contains page object for Amazon home page.
Limited to search functionality only.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AmazonHomePage:

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = 'https://www.amazon.com'
    PAGE_TITLE = 'Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more'

    # Element Locators
    SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Go']")

    # Methods

    def load_page(self):
        self.browser.get(self.URL)

    def search_item(self, item):
        search_input = self.browser.find_element(*self.SEARCH_FIELD)
        search_input.send_keys(item + Keys.RETURN)

    def verify_title(self):
        assert self.browser.title == self.PAGE_TITLE
