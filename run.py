from bot.steps import Bot
import time

def main():
    bot = Bot('https://www.nytimes.com/')
    bot.land_page()
    bot.maximize_window()
    bot.click_cookies()
    time.sleep(2)

if __name__ == '__main__':
    main()