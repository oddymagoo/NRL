import requests
from bs4 import BeautifulSoup

url = 'https://www.nrl.com/news/2019/03/12/round-1-nrl-team-lists/'
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
print (soup.prettify())