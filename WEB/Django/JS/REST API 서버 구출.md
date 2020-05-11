# REST API 서버 구출

2020.05.11

## intro

### MTV

- Model : 데이터를 구조화하는 곳
- Template : 데이터 표시하는 곳
- View : 데이터 흘러다니는 곳

### API

Application Programming Interface

개발자용 접점

### 데이터 표기법 

#### {JSON}

**JavaScript Object Notation**

- JavaScript 객체식 표기법

- cf) XML : eXtended Markup Language (W3C, 1996)
  - JSON 사용하기 이전의 약속
- HTML를 표기법으로 사용불가능한 이유 : Key 값(태그)을 정의 불가능
  - XML은 태그에 제약 X기에 사용가능했었다!

#### JSON vs XML

길이가 더 짧음! => 데이터 용량, 시간, 비용 다 효율적, 싸다는 뜻!

(XML은 닫는 태그도 있어야하기 때문)

## Django REST Framework

**​ :star: Django에서 JSON형식에 맞춰서 Data만 제공한다.** 

앞으로 M <=> V (이전 M -> V -> T)

- 최종 구현하고자 하는 흐름!

  ![image-20200511095414597](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200511095414597.png)

- 이때 `React js`, `Angular js`, `Vue js` 다같은 동작을 한다.
  - 공통점 : JS!
- chrome `json viewer` 확장 프로그램 추가 시 데이터 잘 보일 수 있도록 해준다.

## DJango json 데이터 만들기

#### `faker`

- 사용방법

  1. `pip install faker` : data 넣기 쉬움

  2. `pip install django-extensions` 설치

  3. settings.py 에 installed_apps 에 `django_extensions` 넣어주기 

     => shell plus 사용하기 위해

  4.  `python manage.py shell_plus`

     ```python
     from faker import Faker
     f = Faker()
     f.text()
     f.name()
     f.paragraph()
     ```

---

### models.py

```python
from django.db import models
from faker import Faker

f = Faker()

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @classmethod
    def dummy(cls, n): # n개의 데이터를 만들겠다!
        for _ in range(n):
            cls.objects.create(
                title = f.name(),
                content = f.text()
            )
```

- `Article.dummy(100)` : 100개의 데이터를 만들겠다!

### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [ # 3가지 방법으로 구현가능하나 세번재 방법으로 사용할 예정!
    path('json1/', views.article_list_json_1),
    path('json2/', views.article_list_json_2),
    path('json3/', views.article_list_json_3),
]
```

### 방법 3가지!

##### 원래 이전에 사용했던 코드 (참고)

```python
from django.shortcuts import render
from .models import Article

def article_list_html(request):
    articles = Article.objects.all()
    context = { 'articles':articles }
    return render(request, 'board/article_list.html', context)
```

#### 1. 노가다 (두번다시 볼일 없는 코드)

```python
# views.py
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http.response import JsonResponse # 데이터 JSON으로 보내기!

from .models import Article

def article_list_json_1(request):
    articles = Article.objects.all()
    # articles : QuerySet이기에 list, dictionary 아님!
    # JSON : [] 또는 {}로 시작함 (추가로 "" 사용)
    data = []
    for article in articles:
        data.append({
            'article_id': article.id,
            'title': title,
            'content': content,
            'created_at': created_at,
            'updated_at':updated_at,
        })
    return JsonResponse(data, safe=False)
```

- JsonResponse에서 `safe parameter`가 False라고 해야한다.

  false일 때 딕셔너리가 아닌 것을 보낼 수 있다.

#### 2.  django core serializer (사용 X 예정)

```python
from django.http.response import JsonResponse, HttpRespnse 

# views.py
@require_GET
def article_list_json_2(request):
    from django.core import serializers
    
    articles = Article.objexts.all() # 데이터 있는 곳
    data = serializers.serialize('json', articles) # articles 데이터를 json으로 바꿔달라.
    return JsonResponse(data, safe=False)
	return HttpResponse(data, content_type='application/json')
```

- 하나의 스트링으로 그대로 통째로 내보내도록 만들어준다.
- 한방에 가능! mdeol, pk 다 나옴 => 데이터 길이가 보고싶었던(원하는 것)보다 많이 보내진다.  == field 지정 불가능

#### 3. django REST framework :happy: "최종적 방법"

##### 사용전 준비

- 터미널에 `pip install djangorestframwork` 설치
- settings.py 에 INSTALLED_APPS 에 `rest_framework` 추가

##### 사용하기

ModelForm과 방법 , 기능 유사

1. `serializers.py` 파일 생성하기

   `ArticleSerializer` 만들기

   ```python
   from rest_framework import serializers
   from .models import Article
   
   
   class ArticleSerializer(serializers.ModelSerializer):
       class Meta:
           model = Article
           fields = '__all__' 
           # fields = ['title', 'content'] 커스텀 가능
   ```

2. views.py

   ```python
   from rest_framework.response import Response
   from rest_framework.decorators import api_view
   
   from .models import Article
   from .serializers import ArticleSerializer
   
   @api_view(['GET'])
   def article_list_json_3(request):
   	articles = Article.objeCts.all()
       serializer = ArticleSerializer(articles, many=True) # many=True : queryset이기에 사용하는 것, 하나가 아니다!
       # rest_framework 의 serializer를 리턴하려면, Response 사용하기!
       return Response(serializer.data)
   ```

   