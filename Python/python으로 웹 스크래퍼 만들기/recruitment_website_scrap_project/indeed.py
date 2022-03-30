import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
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


def extract_indeed_jobs(last_page):
  # 페이지별로 사이트에서 추출할 jobs에 대한 정보를 담아 리턴하는 함수
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    # jobs에 필요한 데이터 추가 로직
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class': 'job_seen_beacon'})
    for result in results:
      # 가져올 정보 위치의 규칙을 찾아 가져오기
      title = result.find('span', {'title': True}).string
      jobs.append(title)
  return jobs
