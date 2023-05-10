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