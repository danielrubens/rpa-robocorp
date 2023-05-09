from RPA.Browser.Selenium import Selenium

class Bot:
    def __init__(self, url):
        self.url = url
        self.navigator = Selenium()
        self.find = self.navigator.find_element

    def land_page(self):
        self.navigator.open_available_browser(self.url)

    def maximize_window(self):
        self.navigator.maximize_browser_window()

    def click_cookies(self):
        self.find('xpath://button[@data-testid="GDPR-accept"]').click()

    def click_search(self):
        self.find('css:button[data-test-id="search-button"]').click()

    def search_field(self):
        self.find('css:input[data-testid="search-input"]').send_keys("Biden")
        self.find('css:button[data-test-id="search-submit"]').click()

    def click_filter_section(self):
        button_section = self.find('css:button[data-testid="search-multiselect-button"]')
        button_section.click()
        