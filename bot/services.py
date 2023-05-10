import re

def clean(elements):
    texts = [i.text for i in elements]
    return [re.sub(r'\d+', '', i).strip(',') for i in texts]

def select_params(params, treated, elements):
    for i in params:
            for j in range(len(treated) -1):
                if treated[j] == i:
                    elements[j].click()