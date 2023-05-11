from bot.constants import Selector
from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.keys import Keys
from bot.services import clean, select_params, get_dates, generate_fields


class Bot:
    def __init__(self, url):
        self.url = url
        self.navigator = Selenium()
        self.find = self.navigator.find_element
        self.find_elements = self.navigator.find_elements

    def land_page(self):
        self.navigator.open_available_browser(self.url)

    def maximize_window(self):
        self.navigator.maximize_browser_window()

    def click_cookies(self):
        self.find(Selector.COOKIES).click()

    def click_search(self):
        self.find(Selector.SEARCH).click()

    def search_field(self, word):
        self.find(Selector.SEARCH_INPUT).send_keys(word)
        self.find(Selector.SEARCH_SUBMIT).click()

    def click_filter(self, params, filter):
        index = {"section": 0, "type": 1}[filter]
        button = self.find_elements(Selector.MULTISELECT_BUTTON)[index]
        button.click()
        elements = self.find_elements(Selector.MULTISELECT_ELEMENTS)
        treated = clean(elements)
        select_params(params, treated, elements)
    
    def click_filter_section(self, params):
        self.click_filter(params, "section")
    
    def click_filter_type(self, params):
        self.click_filter(params, "type")

    def select_date(self, months):
        start_date, end_date = get_dates(months)
        button_date = self.find(Selector.DATE_BUTTON)
        button_date.click()
        button_specify_date = self.find(Selector.SPECIFY_DATE_BUTTON)
        button_specify_date.click()
        start_date_field = self.find(Selector.START_DATE_FIELD)
        start_date_field.clear()
        start_date_field.send_keys(start_date)
        end_date_field = self.find(Selector.END_DATE_FIELD)
        end_date_field.clear()
        end_date_field.send_keys(end_date)
        end_date_field.send_keys(Keys.ENTER)
    
    def get_results(self):
        results = self.find_elements(Selector.BODEGA_RESULTS)
        return [generate_fields(i) for i in results]