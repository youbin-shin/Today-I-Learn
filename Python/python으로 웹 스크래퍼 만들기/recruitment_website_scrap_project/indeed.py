import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  # indeed 사이트에서 마지막 페이지를 가져오는 함수
  result = requests.get(URL)
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
  return {
    'title': title, 
    'company': company, 
    'location': location
  }

def extract_jobs(last_page):
  # 페이지별로 사이트에서 추출할 jobs에 대한 정보를 담아 리턴하는 함수
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    # jobs에 필요한 데이터 추가 로직
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class': 'job_seen_beacon'}) 
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  # indeed 취업 사이트에서 python 직무 채용 목록 스크랩트하는 함수
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
