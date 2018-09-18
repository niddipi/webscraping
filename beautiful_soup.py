import requests
from bs4 import BeautifulSoup
from pprint import pprint

urls = []
for i in range(1,5):
    pages = "https://directory.singaporefintech.org"
    urls.append(pages)

Data = []
hrefs = []
for info in urls:
    page = requests.get(info)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('div', attrs ={'class' :'sabai-directory-title'})
    for link in links:
        Data.extend([a['href'].encode('ascii') for a in link.find_all('a', href=True) if a.text])
pprint (Data)
