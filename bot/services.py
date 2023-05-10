import re
from datetime import datetime, timedelta

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

def generate_fields(result, figure):
    text = result.text.split('\n')
    figurename = figure.split('/')[-1]
    quantity = word_count(text[3]) + word_count(text[2])
    my_dict = {"title": text[2], "date": text[-1], "description": text[3], "words": quantity,
                "image_src": figure, "image_name": figurename}
    return my_dict