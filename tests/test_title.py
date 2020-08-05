import pytest
from pages.home_page import AmazonHomePage

@pytest.mark.smoketest
def test_amazon_title(browser):
    home_page = AmazonHomePage(browser)

    # navigate to Amazon home page
    home_page.load_page()

    # verify Amazon home page title is matching expected title
    home_page.verify_title()
