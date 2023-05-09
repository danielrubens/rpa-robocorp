from RPA.Browser.Selenium import Selenium

class Bot:
    def __init__(self, url):
        self.url = url
        self.navigator = Selenium()

    def land_page(self):
        self.navigator.open_available_browser(self.url)

    def maximize_window(self):
        self.navigator.maximize_browser_window()