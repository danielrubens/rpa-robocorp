from bot.steps import Bot
from bot.writer import Writer
import time

def main():
    bot = Bot('https://www.nytimes.com/')
    bot.land_page()
    bot.maximize_window()
    bot.click_cookies()
    time.sleep(2)
    bot.click_search()
    time.sleep(2)
    bot.search_field()
    time.sleep(3)
    bot.click_filter_section(['Blogs', 'Business'])
    time.sleep(2)
    bot.click_filter_type(['Article'])
    time.sleep(2)
    bot.select_date(2)
    time.sleep(2)
    news = bot.get_results()
    writer = Writer(news)
    writer.load_xml()
    writer.save_images()

if __name__ == '__main__':
    main()