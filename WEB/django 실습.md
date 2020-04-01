# django 실습

## 준비과정 정리

1. 터미널 창에서 `cd practice/(원하는 폴더로)` 로 작업할 폴더로 이동
2. `mkdir (폴더 생성 ex.exercise)` 후 `cd exercise` 그 폴더로 이동
3. `dgango-admin startproject (프로젝트 파일 명 ex.intro)` 프로젝트 생성
4. `cd intro` 생성한 프로젝트로 들어가서 `ls` 검색
5. `manage.py` 확인 후 

### posts

> 2020.03.30

- template 활용
  - DTL (django Template Language)

1. urls.py

   ```python
   # urlpatterns 리스트에 추가
   path('posts/<int:id>/', views.posts),
   ```

2. views.py

   ```python
   def posts(request, id):
       content = 'Life is short, you need python!'
       replies = ['유익한 글이네요!', '재밌어요.', '도움이 되네요']
       user = 'admin'
       no_replies = []
       context = {
           'id' : id,
           'content': content,
           'replies': replies,
           'no_replies': no_replies,
           'user': user,
       }
       return render(request, 'post.html', context)
   ```

3. pages/templates/post.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Document</title>
   </head>
   <body>
       <h1>{{ id }}번째 글입니다.</h1>
       <p>{{ content }}</p>
       <p>{{ content|length }}글자</p>
       <p>{{ content|truncatechars:10 }}</p>
       <hr>
       <!--댓글 출력 반복-->
       <h2>댓글</h2>
       <ul>
       {% for reply in replies %}
           <li>{{ reply }}</li>
       {% endfor %}
       </ul>
       <ul>
       {% for reply in replies %}
           <li>댓글{{ forloop.counter }} : {{ reply }}</li>
       {% endfor %}
       </ul>
       <ul>
       {% for reply in no_replies %}
           <li>댓글{{ forloop.counter }} : {{ reply }}</li>
           {% empty %}
           <p>댓글이 없습니다. 작성해주세요.</p>
       {% endfor %}
       </ul>
       {% if user == 'admin' %}
           <p>수정, 삭제</p>
       {% else %}
           <p>관리자 권한이 없습니다.</p>
       {% endif %}
   </body>
   ```

   - `forloop.counter` : for ~ endfor 안에서 사용
   - `empty` : 비어있을 때 사용
   - `{{ content|truncatechars:10 }}` : 글자수 잘라서 보여주는 기능
   - `|` : filter 

4. base.html을 이용하여 작성

   - base.html

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Django 기초 - pages</title>
   </head>
   <body>
       <h1>Django 기초 문법 학습</h1>
       {% block body %}
       {% end block %}
   </body>
   ```

   - post.html

   ```html
   {% extends 'base.html' %}
   
   
   {% block css %}
   <style>
       h1 {
           color: blue;
       }
   </style>
   {% endblock %}
   
   {% block body %}
       <h1>{{ id }}번째 글입니다.</h1>
       <p>{{ content }}</p>
       <p>{{ content|length }}글자</p>
       <p>{{ content|truncatechars:10 }}</p>
       <hr>
       <!--댓글 출력 반복-->
       <h2>댓글</h2>
       <ul>
       {% for reply in replies %}
           <li>{{ reply }}</li>
       {% endfor %}
       </ul>
       <ul>
       {% for reply in replies %}
           <li>댓글{{ forloop.counter }} : {{ reply }}</li>
       {% endfor %}
       </ul>
       <ul>
       {% for reply in no_replies %}
           <li>댓글{{ forloop.counter }} : {{ reply }}</li>
           {% empty %}
           <p>댓글이 없습니다. 작성해주세요.</p>
       {% endfor %}
       </ul>
       {% if user == 'admin' %}
           <p>수정, 삭제</p>
       {% else %}
           <p>관리자 권한이 없습니다.</p>
       {% endif %}
   {% endblock %}
   ```

5. 화면

![4](https://user-images.githubusercontent.com/60081201/77871782-2330c300-7280-11ea-84a4-1debea2a9336.JPG)

### base.html로 모든 templates 적용하기

1. base.html 생성

```htmL
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Django 기초 - pages</title>
</head>
<body>
    <h1>Django 기초 문법 학습</h1>
    {% block body %}
    {% end block %}
</body>
</html>
```

2. 확장해서 사용할 html 에 head, body 다지워주고 블록들을 만들어주면 된다.

   기본으로 할 html  **맨위에 최!상!단! 고정**`{% extends 'base.html' %}` (두개를 확장할 수 X)

   이름 지칭해주는거 동일하게!

```html
{% extends 'base.html' %}

{% block body %}
    """ body에 들어갈 부분 추가하면 끝 """
{% endblock %}
```



### post + 사용자 입력 보여주기

다중 app활용

---

### ping pong

> 2020.03.31

- ping : 정보 받기
- pong : 정보 출력

#### 사용자 정보 받기 form

1. urls.py

   ```python
   # boards/urls.py
   urlpatterns = [
       path('ping/', views.ping),
   ]
   ```

2. views.py

   ```python
   # boards/views.py
   def ping(request):
       return render(request, 'boards/ping.html')
   ```

3. ping.html

   - form : action 설정 중요
   - action : 정보를 처리할 함수를 내부적으로 urls 만들어주는 것

   ```html
   <!-- boards/templates/boards/ping.html -->
   <form action="/boards/pong/">
       메시지 입력 : <input type="text" name="message">
       <input type="submit">
   </form>
   ```

#### 정보처리

1. urls.py

   ```python
   # boards/urls.py
   urlpatterns = [
       path('ping/', views.ping),
       path('pong/', views.pong)
   ]
   ```

2. views.py

   ```python
   # boards/views.py
   from requests import requests
   def ping(request):
       return render(request, 'boards/ping.html')
   
   def pong(request):
       # 정보 받기
       messages = request.GET.get('message') #--> input name과 동일하게!
       # template 변수
       context = {
           'messages': messages
       }
       return render(request, 'boards/pong.html', context)
   ```

3. pong.html

   ```html
   <h1>{{ message }}</h1>
   ```

--> 흐름, login 익숙해지기

---

- view --> url, request (요청 관련 정보), return render()
- template --> render 함, html, DTL, 반복 조건 필터
- model ★ --> DB

### model

DB에 대한 model --> 서비스에 대한 영향

#### 1. 스키마

스키마를 통해 각각 colum들의 타입 지정 가능!!

효과적으로 관리하기 위해서

각 열들에 데이터 타입을 가질지 미리 정의

#### 2. table

큰 데이터 베이스에는 여러개의 table 존재

행과 열로 구성

- 행 = **row** = 레코드
- 열 = **column** = 속성 = 필드

### DB 조작 언어

- SQL
- ORM : 이용하여 조작할 예정
  - Object Relational(DB) Mapper 객체 관계 매핑 
  - 파이썬 객체 조작(메서드 호출)으로 DB를 조작한다.

### 실습

1. 새로운 프로젝트 만들고 setting에서 '*', ko-kr 기본 세팅

2. 앱 만들기  articles

   1. setting에서 INSTALLED_APPS에 앱 등록
   2. urls 에 등록 (프로젝트 별 관리를 위해)

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('articles/', include('articles.urls'))
   ]
   ```

   3. articles에 새로운 파일 urls.py 생성

      뼈대 만들기

   ```python
   from django.urls import path
   
   urlpatterns = [
   ]
   ```

3. 본격적으로 model 시작

   클래스 만들기

   DB 모델링

   ```python
   # articles/models.py
   from django.db import models
   
   # Create your models here.
   class Article(models.Model):
       title = models.CharField(max_length=140)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

4. 터미널 창에 `python.manage.py makemigrations` 입력 : 모델링 한것을 DB에 반영할 준비

   이후 `python manage.py migrate` 입력 : DB에 반영

5. DB에 반영되어 있는지 살펴보기 위해서 `admin.py` 활용

   ```python
   from django.contrib import admin
   
   # Register your models here.
   from .models import Article
   
   admin.site.register(Article)
   ```

#### 직접 article 조작

1. 터미널에 `pip install django-extensions ipython` 설치하기

2. 터미널에 `python manage.py shell_plus `  --> 주피터 노트북 같다

3. 데이터 게시물의 object 조작 가능

4. method 조작

   CRUD method

   - Create 생성

   - Read 조회

     id : PrimaryKey(PK)

     - Article.objects.all()
     - Article.objects.get(id=2) 

   - Update 수정

     

   - Delate 삭제

     - a.delete()

## 0401

### cSS와 같이 정적 가져올때

![image-20200401095308873](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200401095308873.png)

![image-20200401095422615](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200401095422615.png)

![image-20200401102354945](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200401102354945.png)

gitignore

> https://www.gitignore.io/

![image-20200401104904958](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200401104904958.png)

gittignore 해야할걸 모르겟으면 구글에 gitignore 검색!!이거에 django 치면 다나옴

### git

project 에서 git init 하고

touch .gitignore 명령어로 만들기

> 언어는 퀄리티가 낮아서 github.gitignore 에서 추가하는 것이 좋다
>
> https://github.com/github/gitignore

![image-20200401121932727](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200401121932727.png)

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/

django coding style 

import 순서