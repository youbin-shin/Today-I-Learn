# Web scraper with python

## 0. Introduction

### Python

python 언어는 아래 목록 모두 구현가능하다.

- 웹 개발
- Data Science
- Machine Learning

> tip) python code를 브라우저에서 작성할 수 있게 도와주는 사이트: repl.it

### Web Scraping

- 의미: 웹사이트에서 정보 추출
- 구현 방향: 구글 크롬 이용
  - Online Compiler가 구글 크롬 안에서 동작하기 때문



## 1. Theory

> web scraping을 하기 위해 필요한 python 이론 

- Data Types of Python
  - str, int, float, bool, NoneType
- Lists in Python
  - sequence type
    - list
    - tuple

- module
  - 기능의 집합
  - import하여 사용 가능 (tip. 사용할 것만 `from import`를 통해 불러오는 것이 효율적이다!)



## 2. Building a job Scrapper

- What is Web Scrapping?
  - 웹 상의 데이터를 추출하는 것
  - = web index mining = data mining

- Navigating with Python

  - requests

    - ```python
      import requests
      ```

    - requests 모듈은 파이썬에서 요청을 만드는 기능이 모여있음
    - https://pypi.org/project/requests2/

  - beautiful Soup

    ```python
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    ```

    - 편리한 라이브러리로 html 정보를 추출하기 유용한 package -> 데이터 추출!
    - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

- Web scraping procedure

  1. scrap할 사이트의 url 접근하기

  2. 페이지가 몇개인지 확인하기

  3. 페이지 하나씩 들어가서 정보 가져오기

     ```python
     import requests
     
     res = requests.get("{url}")
     print(res.text)
     ```

     res.text안에 html에서 정보를 가져와야 한다!
     BeautifulSoup을 이용하여 필요한 페이지네이션 데이터를 찾는다.

  4. 페이지 정보를 저장하여 마지막 페이지 찾기
  5. 페이지를 계속해서 request하기

### 실습 코드
```python
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
pagination = indeed_soup.find('div', {'class': 'pagination'})

pages = pagination.find_all('a')
spans = []
for page in pages[:-1]:
  spans.append(int(page.find('span').string)) # == spans.append(int(page.string))
last_page = pages[-1]

```
