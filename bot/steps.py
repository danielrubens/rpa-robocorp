from RPA.Browser.Selenium import Selenium

class Bot:
    def __init__(self, url):
        self.url = url
        self.navigator = Selenium()

    def land_page(self):
        self.navigator.open_available_browser(self.url)

    def maximize_window(self):
        self.navigator.maximize_browser_window()

    def click_cookies(self):
        accept = self.navigator.find_element('xpath://button[@data-testid="GDPR-accept"]')
        accept.click()

    def click_search(self):
        search = self.navigator.find_element('css:button[data-test-id="search-button"]')
        search.click()
