import time
from bot.steps import Bot
from bot.writer import Writer
from functools import wraps


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
    bot = Bot('https://www.nytimes.com/')
    bot.land_page()
    bot.maximize_window()
    bot.click_cookies()
    bot.click_search()
    bot.search_field()
    bot.click_filter_section(['Blogs', 'Business'])
    bot.click_filter_type(['Article'])
    bot.select_date(2)
    news = bot.get_results()
    writer = Writer(news)
    writer.load_xml()
    writer.save_images()

if __name__ == '__main__':
    main()