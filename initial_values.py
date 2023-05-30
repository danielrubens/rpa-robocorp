import configparser

class Constants:
    config = configparser.ConfigParser()
    config.read('config.ini')

    URL = config.get('search', 'URL')
    SEARCH = config.get('search', 'SEARCH')
    SECTION = config.get('search', 'SECTION').split(',')
    TYPE = [config.get('search', 'TYPE')]
    MONTHS = int(config.get('search', 'MONTHS'))