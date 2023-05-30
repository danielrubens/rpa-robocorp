import configparser

class Constants:
    config = configparser.ConfigParser()
    config.read('config.ini')

    URL = 'https://www.nytimes.com/'
    SEARCH = config.get('search', 'SEARCH')
    SECTION = config.get('search', 'SECTION').split(',')
    TYPE = [config.get('search', 'TYPE')]
    MONTHS = int(config.get('search', 'MONTHS'))
    # SEARCH = 'Biden'
    # SECTION = ['Blogs', 'Business']
    # TYPE = ['Article']
    # MONTHS = 2