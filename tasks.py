import time
from bot.steps import Bot
from bot.writer import Writer
from functools import wraps
from initial_values import Constants



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
    bot = Bot(Constants.URL)
    bot.land_page()
    bot.maximize_window()
    bot.click_cookies()
    bot.click_search()
    time.sleep(2)
    bot.search_field(Constants.SEARCH)
    time.sleep(2)
    bot.click_filter_section(Constants.SECTION)
    time.sleep(2)
    bot.click_filter_type(Constants.TYPE)
    bot.select_date(Constants.MONTHS)
    news = bot.get_results()
    writer = Writer(news)
    writer.load_xml()
    writer.save_images()

if __name__ == '__main__':
    main()