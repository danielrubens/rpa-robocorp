import re

def clean(elements):
    sections = [re.sub(r'\d+', '', i.text) for i in elements]
    treated = sections[0].replace('\n', ',').split(',')
    return [i for i in treated if i!= '']