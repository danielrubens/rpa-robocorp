import re
from bot.services import clean, select_params
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

    def click_filter_date(self):
        button_date = self.find('css:button[data-testid="search-date-dropdown-a"]')
        button_date.click()

    def click_filter_section(self):
        button_section = self.navigator.find_elements('css:button[data-testid="search-multiselect-button"]')[0]
        button_section.click()
        
    def click_filter_type(self):
        button_type = self.navigator.find_elements('css:button[data-testid="search-multiselect-button"]')[1]
        button_type.click()

    def get_filter_section(self, params):
        elements = self.navigator.find_elements('class:css-1qtb2wd')
        treated = clean(elements)
        select_params(params, treated, elements)
