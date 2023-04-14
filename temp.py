import scrap
from datetime import date
from csv import DictReader


def addNewsToDB():
    with open(f"news_csv/{date.today()}.csv", "r") as rf:
        csv_reader = DictReader(rf)
        return list(csv_reader)


print(addNewsToDB()[0].get("Headline"))
