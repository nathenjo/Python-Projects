import requests
import re
import inflection
from bs4 import BeautifulSoup
import urllib.request

url = requests.get('https://dailysmarty.com/topics/python')
def web_scraper(url):
    new_url = url.text

    website = BeautifulSoup(new_url, 'html.parser')

    list_of_headings = website.findAll('h2')
    links_list = []

    for link in website.findAll('a', attrs={'href': re.compile("posts/")}):
        links_list.append(link.get('href'))

    for title in links_list:
        title = inflection.titleize(title)
        print(title.replace('/Posts/', ''))


web_scraper(url)