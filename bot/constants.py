class Selector:
    COOKIES = "xpath://button[@data-testid='GDPR-accept']"
    SEARCH =  "css:button[data-test-id='search-button']"
    SEARCH_INPUT = "css:input[data-testid='search-input']"
    SEARCH_SUBMIT = "css:button[data-test-id='search-submit']"
    MULTISELECT_BUTTON = 'css:button[data-testid="search-multiselect-button"]'
    MULTISELECT_ELEMENTS = 'class:css-1qtb2wd'
    DATE_BUTTON = 'class:css-p5555t'
    SPECIFY_DATE_BUTTON = 'css:[aria-label="Specific Dates"]'
    START_DATE_FIELD = 'css:[aria-label="start date"]'
    END_DATE_FIELD = 'css:[aria-label="end date"]'
    BODEGA_RESULTS = 'xpath://li[@data-testid="search-bodega-result"]'
    TITLE = './/h4[@class="css-2fgx4k"]'
    DATE = './/span[@data-testid="todays-date"]'
    DESCRIPTION = './/p[@class="css-16nhkrn"]'
    IMAGE = './/img'
