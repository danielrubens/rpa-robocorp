from bot.steps import Bot

def main():
    bot = Bot('https://www.nytimes.com/')
    test = bot.land_page()
    print(test)


if __name__ == '__main__':
    main()