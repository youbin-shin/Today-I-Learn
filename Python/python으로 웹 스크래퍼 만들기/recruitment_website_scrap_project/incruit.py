import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://job.incruit.com/jobdb_list/searchjob.asp?occ3=16930&articlecount={LIMIT}"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pages = soup.find('p', {'class': 'sqr_paging'}).find_all('a')

  last_page = 1
  for page in pages:
    page = page.string
    try:
      page = int(page)
      if last_page < page:
        last_page = page
    except ValueError:
      pass
  return last_page

def extract_job(html):
  title = html.find('span', {'class': 'accent'}).find('a', {'class': 'links'})['title']
  company = html.find('div', {'class': 'check_list_r'}).find('span', {'class': 'links'}).find('a', {'class': 'strong'})['title']
  location = html.find_all('p', {'class': 'details_txts firstChild'})[-1].find('em').get_text()
  return {
    'title': title,
    'company': company,
    'location': location
  }

def extract_jobs(last_page):
  jobs = []
  for page in range(1, last_page + 1):
    result = requests.get(f'{URL}&page={page}')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find('tbody').find_all('tr')
    for result in results:
      job = extract_job(result)
      print(job)
      jobs.append(job)

  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
