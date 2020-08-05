from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AmazonSearchResultPage:

    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = 'https://www.amazon.com/s?k=nike+air+max&ref=nb_sb_noss'
    PAGE_TITLE = 'Amazon.com : '

    # Element Locators
    SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Go']")

    # Methods

    def load_page(self):
        self.browser.get(self.URL)

    def search_item(self, item):
        search_input = self.browser.find_element(*self.SEARCH_FIELD)
        search_input.send_keys(item + Keys.RETURN)

    def verify_title(self, item):
        assert self.browser.title == self.PAGE_TITLE + item

