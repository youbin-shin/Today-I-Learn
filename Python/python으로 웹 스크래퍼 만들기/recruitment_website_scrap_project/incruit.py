import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://job.incruit.com/jobdb_list/searchjob.asp?occ3=16930&today=y&articlecount={LIMIT}"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pages = soup.find('p', {'class': 'sqr_paging'}).find_all('a')
  print(pages)
  return


def get_jobs():
  last_page = get_last_page()
