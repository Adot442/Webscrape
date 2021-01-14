import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pathlib

def main():
    URL = 'https://realpython.com/beautiful-soup-web-scraper-python/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    output = ""

    output += "\nAll the big headers are:\n"
    output += findAllText("h1", soup)
    output += "\n\nMedium headers are:\n"
    output += findAllText("h2", soup)
    output += "\n\nSmallest headers are:\n"
    output += findAllText("h3", soup)
    fileOutput(output)


def findAllText(x, soup):
    out = soup.find_all(str(x))
    output = ""

    for item in out:
        output += str(item.text) + "\n"

    return output


def fileOutput(output):
    path = (pathlib.Path(__file__).parent.absolute())
    now = datetime.today().date()

    f = open(str(path) + "/Attachment " + str(now) + ".txt", 'w+')
    f.write(output)
    f.close()
    

main()