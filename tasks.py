import time
from bot.steps import Bot
from bot.writer import Writer
from functools import wraps
from initial_values import Constants
from RPA.Robocorp.WorkItems import WorkItems



def handle_exceptions_and_delay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(2)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred in function '{func.__name__}': {str(e)}")
    return wrapper


@handle_exceptions_and_delay
def main():
    wi = WorkItems()
    wi.get_input_work_item()
    SEARCH = wi.get_work_item_variable("SEARCH")
    SECTION = wi.get_work_item_variable("SECTION")
    MONTHS = wi.get_work_item_variable("MONTHS")
    bot = Bot(Constants.URL)
    bot.land_page()
    bot.maximize_window()
    bot.click_cookies()
    bot.click_search()
    time.sleep(2)
    # bot.search_field(Constants.SEARCH)
    bot.search_field(SEARCH)
    time.sleep(2)
    # bot.click_filter_section(Constants.SECTION)
    bot.click_filter_section(SECTION)
    time.sleep(2)
    bot.click_filter_type(Constants.TYPE)
    # bot.select_date(Constants.MONTHS)
    bot.select_date(MONTHS)
    news = bot.get_results()
    writer = Writer(news)
    writer.load_xml()
    writer.save_images()

if __name__ == '__main__':
    main()