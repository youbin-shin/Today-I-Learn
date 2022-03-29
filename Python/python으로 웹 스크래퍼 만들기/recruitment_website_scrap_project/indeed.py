import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find('div', {'class': 'pagination'})
  links = pagination.find_all('a')

  pages = []
  for link in links[:-1]:
    pages.append(int(link.string)) # == pages.append(int(link.string))

  last_page = pages[-1]
  return last_page


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    # jobs에 필요한 데이터 추가 로직
  return jobs
