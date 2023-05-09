from bot.steps import Bot

def main():
    bot = Bot('https://www.nytimes.com/')
    bot.land_page()
    bot.maximize_window()

if __name__ == '__main__':
    main()