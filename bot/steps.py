from bot.services import clean, select_params
from RPA.Browser.Selenium import Selenium
from datetime import datetime, timedelta

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

    # def click_filter_date(self):
    #     button_date = self.find('css:button[data-testid="search-date-dropdown-a"]')
    #     button_date.click()

    def click_filter(self, params, filter):
        index = {"section": 0, "type": 1}[filter]
        button = self.navigator.find_elements('css:button[data-testid="search-multiselect-button"]')[index]
        button.click()
        elements = self.navigator.find_elements('class:css-1qtb2wd')
        treated = clean(elements)
        select_params(params, treated, elements)
    
    def click_filter_section(self, params):
        self.click_filter(params, "section")
    
    def click_filter_type(self, params):
        self.click_filter(params, "type")

    def select_date(self, months):
        if months == 0:
            months = 1
        start_date = (datetime.now() - timedelta(days=30 * months - 1)).strftime("%m/%d/%Y")
        end_date = datetime.now().strftime("%m/%d/%Y")
        button_date = self.find('class:css-p5555t')
        button_date.click()
        button_specify_date = self.find('css:[aria-label="Specific Dates"]')
        button_specify_date.click()
        start_date_field = self.find('css:[aria-label="start date"]')
        start_date_field.clear()
        start_date_field.send_keys(start_date)


