import re
from datetime import datetime, timedelta
from bot.constants import Selector

def clean(elements):
    texts = [i.text for i in elements]
    return [re.sub(r'\d+', '', i).strip(',') for i in texts]

def select_params(params, treated, elements):
    for i in params:
        for j in range(len(treated) -1):
            if treated[j] == i:
                elements[j].click()

def get_dates(months):
    if months == 0:
        months = 1
    start_date = (datetime.now() - timedelta(days=30 * months - 1)).strftime("%m/%d/%Y")
    end_date = datetime.now().strftime("%m/%d/%Y")
    return (start_date, end_date)

def word_count(text):
        return len(text.split())

def has_money(text):
    pattern = r'(\$[\d,]+(\.\d+)?|\d+(\.\d+)?\s*(dollars|USD))'
    money_representation = re.search(pattern, text)
    return 'True' if money_representation is not None else 'False'

def generate_fields(i):
    title = i.find_element(by='xpath', value=Selector.TITLE).text
    date = i.find_element(by='xpath', value=Selector.DATE).text
    description = i.find_element(by='xpath', value=Selector.DESCRIPTION).text
    image_url = i.find_element(by='xpath', value=Selector.IMAGE).get_attribute('src')
    image_name = image_url.split('/')[-1].split('?')[0]
    my_dict = { "title": title, "date": date, "description": description,
                "image_url": image_url, "image_name": image_name,
                "qty_words": word_count(title) + word_count(description),
                "has_money": has_money(description) or has_money(title)}
    return my_dict
