2020.03.30

### django 어떻게 동작하는가?

1. url 을 정의한다.
2. Views.py에 실행할 함수를 만든다.
3. 변환할 html 파일을 만든다.

#### `render()`[¶](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#render)

- `render`(*request*, *template_name*, *context=None*, *content_type=None*, *status=None*, *using=None*)

핵심은 MTV 에서 T가 단순히 html이 아니라 실제로 html 만들어나가는 template 엔진이 존재한다 기억하기

- 흔히 실수 : 주석처리는 {#여기에 주석쓰기#}

https://docs.djangoproject.com/ko/2.1/ref/templates/language/

https://docs.djangoproject.com/ko/2.1/ref/templates/builtins/







## 문법 정리

### 반복문

```html
{% for reply in replies %}
	<li>{{ reply }}</li>
{% endfor %}
```

DTL에서 연산 X, python 코드 X

--> 연산은 views.py에서 완료! context에 완료한 계산된 결과를 보여주는 것!!

- {{ forloop.counter }}
- {{ forloop.counter0 }}
- {% empty %}

### 조건문

```html
{% if user == 'admin' %}
	<p>관리자 입니다.</p>
{% else %}
	<p>권한이 없습니다.</p>
{% endif %}
```

### built-in tag, filter

```html
{{ content|length }}
{{ content|truncatechars:10 }}
```

