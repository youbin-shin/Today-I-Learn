# django 실습

## 준비과정 정리

1. 터미널 창에서 `cd practice/(원하는 폴더로)` 로 작업할 폴더로 이동
2. `mkdir (폴더 생성 ex.exercise)` 후 `cd exercise` 그 폴더로 이동
3. `jdango-admin startproject (프로젝트 파일 명 ex.intro)` 프로젝트 생성
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





