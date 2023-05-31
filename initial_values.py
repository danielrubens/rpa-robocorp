import configparser
from RPA.Robocorp.WorkItems import WorkItems

class Constants:
    config = configparser.ConfigParser()
    config.read('config.ini')

    wi = WorkItems()
    wi.get_input_work_item()

    URL = config.get('search', 'URL')
    SEARCH = wi.get_work_item_variable("SEARCH")
    SECTION = wi.get_work_item_variable("SECTION")
    MONTHS = wi.get_work_item_variable("MONTHS")
    TYPE = [config.get('search', 'TYPE')]