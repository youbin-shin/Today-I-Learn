import requests
from bs4 import BeautifulSoup

LIMIT = 50
BASE_URL = "https://kr.indeed.com"

def get_last_page(url):
  # indeed 사이트에서 마지막 페이지를 가져오는 함수
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find('div', {'class': 'pagination'})
  links = pagination.find_all('a')

  pages = []
  for link in links[:-1]:
    pages.append(int(link.string)) # == pages.append(int(link.string))

  last_page = pages[-1]
  return last_page

def extract_job(html):
  # 가져올 정보 위치의 규칙을 찾아 가져오기
  title = html.find('span', {'title': True}).string
  company = html.find('span', {'class': 'companyName'}).string 
  location = html.find('div', {'class': 'companyLocation'}).get_text()
  apply_part_link = html['href']
  return {
    'title': title, 
    'company': company, 
    'location': location,
    'apply_link': f'{BASE_URL}{apply_part_link}'
  }

def extract_jobs(last_page, url):
  # 페이지별로 사이트에서 추출할 jobs에 대한 정보를 담아 리턴하는 함수
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed Pages: {page}")
    result = requests.get(f"{url}&start={page*LIMIT}")
    # jobs에 필요한 데이터 추가 로직
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('a', {'class': 'tapItem'})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  # indeed 취업 사이트에서 word에 해당하는 직무 채용 목록 스크랩트하는 함수
  url = f"{BASE_URL}/jobs?q={word}&limit={LIMIT}"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs
