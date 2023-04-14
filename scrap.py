import requests
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter
from datetime import date


def scrap_news_data(url):
    url = url
    r = requests.get(url)
    html_content = r.content

    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup.prettify())

    links = []
    headlines = []
    artiles_scrap = soup.body.div.ol.find_all(
        "a", class_="group-hover:shadow-underline-franklin")
    for l in artiles_scrap:
        links.append(url + l.get("href"))
        headlines.append(l.text)

    authors = []
    authors_scrap = soup.body.div.ol.find_all(
        "a", class_="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8")
    for a in authors_scrap:
        authors.append(a.text)

    date_scrap = soup.body.div.ol.find_all(
        "span", class_="text-gray-63 dark:text-gray-94")

    dates = []
    for d in date_scrap:
        dates.append(d.text)

    field_name = ["Headline", "Link", "Author", "Date"]

    with open(f"news_csv/{date.today()}.csv", "w", newline="") as wf:
        csv_writer = DictWriter(wf, fieldnames=field_name)
        csv_writer.writeheader()
        for data in range(len(headlines)):
            csv_writer.writerow({
                "Headline": headlines[data],
                "Link": links[data],
                "Author": authors[data],
                "Date": dates[data]
            })
    with open(f"news_csv/{date.today()}.csv", "r") as rf:
        csv_reader = DictReader(rf)
        return list(csv_reader)
