import os
import requests
import pandas as pd



class Writer:
    def __init__(self, news):
        self.news = news

    def save_images(self):
        for _, element in enumerate(self.news):
            dir = 'output'
            image = element["image_url"]
            image_name = element["image_name"]
            response = requests.get(image)
            if not os.path.exists(dir):
                os.makedirs(dir)
            path = os.path.join(dir, image_name)
            with open(path, "wb") as file:
                file.write(response.content)

    def load_xml(self):
        os.makedirs('output', exist_ok=True)
        output_directory = 'output/new_york_times_scraper.xlsx' 
        columns = ["title", "date", "description", "image_url", "image_name", "qty_words", "has_money"]
        spreadsheet = pd.DataFrame(self.news, columns=columns)
        spreadsheet.to_excel(output_directory)