# django_pjt3 코드 정리

2020.04.22

### 파일 구조

- django_pjt3
  - django_pjt3 - 프로젝트 명
    - settings.py - 전반적인 설정 진행 (앱등록, DIR 설정 등)
    - urls.py - `include`
  - templates
    - base.html :one:
  - accounts - 로그인 관련 앱 :four:
    - urls.py
    - views.py
    - templates/accounts
      - login.html
      - signup.html
  - **community** - 앱
    - admin.py :three:
    - models.py :two:
    - forms.py :two:
    - urls.py  :five:
    - views.py :five:
    - templates/community :five:
      - form.html
      - review_list.html
      - review_detail.html

---

### 코드

#### :one: templates/base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<style>
    nav {
      height: 80px;
    }
</style>
<body>
    <nav class="d-flex justify-content-between align-items-center fixed-top bg-dark">
        <h1 class="text-white ml-5">Community</h1>
        <ul class="d-flex list-inline list-unstyled mb-0 mr-5">
            <li class="mx-3"><a href="/community/" class="text-white text-decoration-none"><h5>Review List</h5></a></li>
            <li class="mx-3"><a href="/community/new_review/" class="text-white text-decoration-none"><h5>New Review</h5></a></li>
            {% if user.is_authenticated %}
            	<p class="text-white">{{ user.username }}님 환영합니다!</p>
            	<a href="{% url 'accounts:logout' %}">로그아웃</a>
            {% else %}
            	<a href="{% url 'accounts:login' %}">로그인</a>
            	<a href="{% url 'accounts:signup' %}">회원가입</a>
            {% endif %}
        </ul>
    </nav>
    <br><br><br><br>
    {% if messages %}
    <div class="messages">
        {% for message in messages %}
        <div class="alert alert-primary" role="alert">{{ message }}</div>
    {% endfor %}
    </div>
    {% endif %}
    <div class="container">
    {% block content %}
    {% endblock %}
    </div>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>
```

#### :two: models.py

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=30)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
```

#### :two: forms.py

```python
from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
```

#### :three: admin.py​

```python
from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', 'updated_at']

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
```

#### :four: accounts - 로그인 관련 앱

##### urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

##### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect ('community:review_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:review_list')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect ('community:review_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect (request.GET.get('next') or 'community:review_list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('community:review_list')
```

##### templates/accounts

- login.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <form action="" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <button>로그인</button>
      </form>
  {% endblock %}
  ```

- signup.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <form action="" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <button>회원가입</button>
      </form>
  {% endblock %}
  ```

#### :five: community u - v - t​

#### urls.py

```python
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('new_review/', views.new_review, name='new_review'),
    path('<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/update/', views.review_update, name='review_update'),
    path('<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:review_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

#### views.py

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ReviewForm, CommentForm
from .models import Review, Comment

# Create your views here.
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/review_list.html', context)


@login_required
def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_detail', review.pk)
        messages.warning(request, '다시 쓰세요.')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)


@login_required
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    form = CommentForm
    context = {
        'review':review,
        'form': form,
    }
    return render(request, 'community/review_detail.html', context)


@login_required
def review_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('community:review_detail', review.pk)
            messages.warning(request, '다시 쓰세요.')
        else:
            form = ReviewForm(instance=review)
        context = {
            'form': form,
        }
        return render(request, 'community/form.html', context)
    else:
        return redirect('community:review_detail', review.pk)


@require_POST
@login_required
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect('community:review_list')
    else:
        return redirect('community:review_detail', review.pk)


@require_POST
@login_required
def comments_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
        return redirect('community:review_detail', review.pk)


@login_required
def comments_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('community:review_detail', review_pk)
```

#### templates/community

- form.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <form action="" method="POST">
          {% csrf_token %}
          {{ form.as_p }}
          <button>작성</button>
      </form>
  {% endblock %}
  ```

- review_list.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      {% for review in reviews %}
          <h3><a href="{% url 'community:review_detail' review.pk %}" class="text-dark text-decoration-none">제목 : {{ review.title }}</a></h3>
          <hr>
      {% endfor %}
  {% endblock %}
  ```

- review_detail.html

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <p>제목 : {{ review.title }}</p>
      <p>작성자: {{ review.user.username }}</p>
      <p>영화 제목 : {{ review.movie_title }}</p>
      <p>랭크 : {{ review.rank }}</p>
      <p>내용 : {{ review.content }}</p>
      <p>생성 시각 : {{ review.created_at }}</p>
      <p>수정 시각 : {{ review.updated_at }}</p>
      {% if review.user == request.user %}
      <a href="{% url 'community:review_update' review.pk %}">수정</a>
      <form action="{% url 'community:review_delete' review.pk %}" method="POST">
          {% csrf_token %}
          <button>삭제</button>
      </form>
      {% endif %}
      <hr>
      <h3>댓글</h3>
  
      {% for comment in review.comment_set.all %}
          <li>{{ comment.user.username }} : {{ comment.content }}</li>
          {% if comment.user == request.user %}
              <form action="{% url 'community:comments_delete' review.pk comment.pk %}" method="POST">
      			{% csrf_token %}
      			<button>댓글 삭제</button>
      		</form>
      	{% endif %}
      {% endfor %}
  
      <form action="{% url 'community:comments_create' review.pk %}" method='POST'>
          {% csrf_token %}
          {{ form }}
          <button>댓글 작성</button>
      </form>
  {% endblock %}
  ```