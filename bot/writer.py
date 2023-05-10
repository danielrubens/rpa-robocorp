import os
import requests
import xlsxwriter

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
        workbook = xlsxwriter.Workbook('output/new_york_times_scraper.xlsx')
        spreadsheet = workbook.add_worksheet()
        columns = ["title", "date", "description", "image_url", "image_name", "qty_words", "has_money"]

        for index, row in enumerate(columns):
            spreadsheet.write(0, index, row)
        
        for index, row in enumerate(self.news):
            values = [
                row["title"],
                row["date"],
                row["description"],
                row["image_url"],
                row["image_name"],
                row["qty_words"],
                row["has_money"]
            ]
            for col_index, value in enumerate(values):
                spreadsheet.write(index + 1, col_index, value)

        workbook.close()

