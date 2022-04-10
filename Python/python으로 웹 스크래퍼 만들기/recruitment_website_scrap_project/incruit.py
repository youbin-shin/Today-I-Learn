import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://job.incruit.com/jobdb_list/searchjob.asp?occ3=16930&articlecount={LIMIT}"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  try:
    # 마지막 페이지로 한번에 이동하는 버튼이 있는 경우 (">>")
    page_info = soup.find('a', {'class': 'f_next_n'})['href']
    last_page = int(page_info.split('&page=')[1])
  except TypeError:
    # 다음 페이지로 넘어가는 버튼 끝만 있는 경우 (">")
    page_info = soup.find('a', {'class': 'next_n'})['href']
    last_page = int(page_info.split('page=')[1])
  except:
    last_page = 1
  return last_page

def extract_job(html):
  title = html.find('span', {'class': 'accent'}).find('a', {'class': 'links'})['title']
  company = html.find('div', {'class': 'check_list_r'}).find('span', {'class': 'links'}).find('a', {'class': 'strong'})['title']
  location = html.find_all('p', {'class': 'details_txts firstChild'})[-1].find('em').get_text(strip=True).strip('\t')
  apply_link =  html.find('span', {'class': 'accent'}).find('a', {'class': 'links'})['href']
  return {
    'title': title,
    'company': company,
    'location': location,
    'apply_link': apply_link
  }

def extract_jobs(last_page):
  jobs = []
  for page in range(1, last_page + 1):
    print(f"Scrapping Incruit Pages: {page}")
    result = requests.get(f'{URL}&page={page}')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find('tbody').find_all('tr')
    for result in results:
      job = extract_job(result)
      jobs.append(job)
      print(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
