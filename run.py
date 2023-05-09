from bot.steps import Bot
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
    bot.click_filter_section()
    time.sleep(3)

if __name__ == '__main__':
    main()