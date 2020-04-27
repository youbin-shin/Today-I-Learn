# Django ~ DB 총정리

### Django 101

#### 1. 프로젝트 및 APP 초기 설정

##### 프로젝트

```bash
$ django-admin startproject (프로젝트 명)
```

- settings.py 
  - `ALLOWED_HOSTS = ['*']` 왜? 배포 url , * 은 모든을 의미함
  - local : TZ(Time Zone), LC(Language Code)

##### APP

```bash
$ python manage.py startapp (앱이름 복수형 권장)
```

- `INSTALLED_APPS` 앱 등록
- urls.py 설정

#### 2. Model 정의 :star:

```python
# models.py
class ____(models.Model):
    title = models.CharFiled(...)
    content = ...
    ...
    user = ForiegnKey() # user_id 이름으로 column 생성
```

#### 3. ModelForm 정의

- Model에 정의한 필드를 HTML 코드들을 만들어준다.

- 모델이 변경되면 column이 자동으로 변경되어 효과적으로 관리할 수 있다

- valid 검증을 해주며 이을 바탕으로 HTML 코드를 만들어준다.

```python
# forms.py

# 기본 흐름
class ArticleForm(forms.ModelForm):
    class Meta: # ArticleForm 에 관련된 내용 정리
        model = 
        fileds = [ ]
```

#### 4. 코드 작성 흐름

하나의 요청을 처리하기 위해서

**U → V → T**

##### urls.py

- 기본 : (path) url => view의 함수 지정

  ```python
  app_name = # app 별 NameSpace
  urlpatterns = [
      path('create/', views.create, name='create') # name : url 변수화
  ]
  ```

  1. 패턴 : url -> view
  2. 이름 설정

##### views.py

중간관리자

함수 (인자 -> 반환 return)

```python
def __(request, pk): # HTTP Request object, variable routing
    
    # Model에서 가져오기 위한 Query method 
    
    # context => template에 반환하기 위한 값
    
    return ___ # HTTP Response object 반환
```

- 반환 방법 
  1. render
  2. redirect

##### templates

DTL을 통해 HTML 생성

- 기본 
  - context 에 넘어온 값들 자유롭게 사용 가능
  - request, user 정보도 사용 가능
    - setting에 `context-pocessors` 를 통해 가능해짐
  - 확장 (상속) : base.html
    - `{% extends '__' %}` 이용하여 사용가능
- `DIR`  먼저 탐색! 이후 `APP_DIRS` INSTALLED_APPS 에 선언된 순서로 탐색
  - articles/templates/articles/html 이렇게 appname 설정하자!

#### Static files

- 앱 폴더안에 만들기 app/static

- DIR 생성

  `{% load static %}` template에 추가하여 사용하기

---

### django / 기본

#### 클래스

- 상속
- 클래스 : 동작 (메서드), 상태 (변수)
  - cf) 함수 : 로직 재사용

#### Name

- Class => Camel Case

- 변수명/메서드 함수 => snake case

- setting.py => 대문자 snake case

  ---

- app  복수형
- model 단수형

#### setting.py

- `AUTH_PASSWORD_VALIDATOR` : 최소 비번 정의, 반복, 이름 유사, 비밀번호 검증과 관련된 설정

#### Auth

- 모델 (User)

- ModelForm/ Form(User())

- 커스텀은 가져다가 상속

  ---

- 회원가입
  
  - User | UserCreationForm | ModelForm
- 로그인
  -  X | AuthenticationForm | Form
  - AuthenticatonForm **request**:star: 에 정보 담겨있음 유의하기!

#### 로그인 흐름

- request 응답
  1. GET 모델폼 html
  2. POST 저장로직 응답은 redirect
     1. 값 받기
     2. 검증
     3. 저장

#### import 정리

- django
  - db
    - models.py
  - urls
    - path
    - include
  - views
    - decorators
  - shortcuts
  - conf
  - contrib
    - auth
      - forms
      - decorators

![0422](https://user-images.githubusercontent.com/60081201/80098769-6264e200-85a8-11ea-9f35-1fcc47473e24.JPG)

---

### 1 : N

### M : N

새로운 테이블이 새로 생성

1:N, 1:N 합쳐진 테이블