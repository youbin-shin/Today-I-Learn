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
    - install
      - window
        ```bash
        python -m pip install requests
        ```
      - mac
        ```bash
        pip install requests
        ```

  - beautiful Soup

    ```python
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.prettify())
    ```

    - 편리한 라이브러리로 html 정보를 추출하기 유용한 package -> 데이터 추출!
    - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - install
      - window
        ```bash
        pip install beautifulsoup4
        ```
      - mac
        ```bash
        pip install beautifulsoup4
        ```

### Web scraping procedure

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

    - 다음 페이지를 갖고 오는 링크를 보기 위해 html a 태크 안에 href를 참고한다. 아래 예시와 같이 다음(2번째) 페이지를 요청하기 위해서는 start=50, 3번째 페이지 요청을 위해서는 start=100 즉 500 * (page_num - 1)의 규칙을 알 수 있다.
      ```html
      <li><a href="/jobs?q=python&amp;limit=50&amp;start=50" aria-label="2" data-pp="gQAyAAABf9DVb-wAAAABzd2DswBoAQIBBxAHA0Sb7C3H5lrLs1hpTcTj5mioNdJ3l7CN_VDNIB1oFzChb7P5_TCp8_3dYwXUnYqTyTBbV4w3x19DrKyMa4nPOj43M7fYaqHi0smRMHPxyKqdnoH092silP-c5bEqRgrBOXwAAA" onmousedown="addPPUrlParam &amp;&amp; addPPUrlParam(this);" rel="nofollow"><span class="pn">2</span></a></li>
      ```
  6. 요청시 가져올 데이터를 beautifulSoup을 이용하여 필요한 데이터만 저장하기



### CSV

What is CSV?
- Comma Separated Values



## 3. Get ready for Django

[django]: https://www.djangoproject.com/

### 알아야 할 개념

- arguments 와 keyword arguments 란?

  - ```python
    # ex 1
    def plus(a, b, *args, **kwargs):
        print(args) # 출력: (1, 1, 1, 3, 3, 3, 3, 3)
        print(kwargs) # 출력: {'this': 'is', 'kwargs': 'args'}
        return a + b
    
    plus(1, 2, 1, 1, 1, 3, 3, 3, 3, 3, 'this': 'is', 'kwargs': 'args')
    ```

    - `*args`: tuple 형태로 positional argument가 많이 있을 것이라는 의미(제한 x)
    - `**kwargs`: dictionary 형태로 keyword argument가 많이 있을 것이라는 의미(제한 x)

  - ```python
    # ex 2) 계산기 로직
    def plus(*args):
        result = 0
        for number in args:
            result += number
        return result
    
    plus(1, 2, 3, 4, 3, 2, 1, 2, 5, 4, 3, 2)
    
    ```

    

- 객체 프로그래밍

  - 기억할 개념: Class, Inheritance(상속), method
  
  - Class: 설계도 같은 것
    ```python
    class Car(): # -> class 기본 형태 
        # properties
        wheels = 4 
        doors = 4
        windows = 4
        seats = 4

    porche = Car() # 클래스를 통해 인스턴스 생성
    print(porche.windows) # 4

    porch.color = "Red"
    print(porche.color) # Red

    ferrari = Car()
    ferrari.color = "Yellow"
    ```
     
  - method: class 안에 있는 함수
    ```python
    class Car(): 
        wheels = 4 
        doors = 4
        windows = 4
        seats = 4

        def start(): # method: class 안에 있는 function
            print("I started")

    def start(): # function
        print("I started")
    ```
     
  - 파이썬은 모든 함수를 하나의 argument와 함께 사용한다.
    [중요] 모든 method의 첫번째 argument는 method를 호출하는 instance 자신이다.
    파이썬은 method를 호출할 때 method의 instance를 첫번째 argument로 사용한다.
    ```python
    # error code
    class Car():
        wheels = 4 
        doors = 4
        windows = 4
        seats = 4

        def start():
            print("I started")

    porche = Car()
    porche.start() # error 발생 - TypeError: start() takes 0 positional arguments but 1 was given

    # correct code
    class Car():
        wheels = 4 
        doors = 4
        windows = 4
        seats = 4

        def start(self):
            print(self.color) # Green
            print("I started")

    porche = Car()
    porche.color = "Green"
    porche.start()

    ```
  

  
    



## 실습 코드

### 실행 방법
  ```bash
  $ cd /recruitment_website_scrap_project
  $ python main.py
  ```

### BeautifulSoup 이용한 개념 정리
- find() vs find_all()
  아래 함수들을 통해 원하는 태그 정보를 가져온다.
  - find(): 첫번째 찾은 결과만 가져옴

  - find_all(): 리스트 전부 가져옴

    - .find_all(recursive=False) : 안에 한 depth 들어가 있는 것들은 패스함

      ```html
      <div class='class'>
          <span>
              1반
              <span>이과</span>
          </span>
          <span>2반</span>
          <span>3반</span>
      </div>
      ```

      - 예시가 위와 같을 경우

        ```python
        results = soup.find_all('span') # 이과도 포함되어 리스트로 나옴
        results = soup.find_all('span', recursive=False) # 1반, 2반, 3반만 리스트로 나옴
        ```

        

- string vs get_text
  태그 내 문장을 가져옴
  - string는 문자열이 없거나 문자열이 많은 경우 None 출력

  - get_text()는 태그 내 문자들을 모두 가져옴
  
    - .get_text(strip=True) : strip기능을 이용하여 원하는 문자열을 제거하여 가져올 수 있음
  
      - ``` python
        # ex) 엔터 삭제
        .get_text(strip=True).strip('\t').strop('\n') 
        ```
