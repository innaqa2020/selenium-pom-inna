import platform
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_version_win = "84"
    chrome_version_mac = "84"

    if 'Win' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_win_{}.exe".format(chrome_version_win))
    elif 'darwin' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac))
    elif 'macOS' in platform.platform():
        browser = webdriver.Chrome("../resources/chromedriver_mac_{}".format(chrome_version_mac))
    else:
        raise Exception("chromedriver is not configured for your Operation System! "
                        "Your Operating System is: {}".format(platform.platform()))

    # wait 10 seconds to pull the DOM
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # when test is done, close ALL windows of the browser
    browser.quit()
