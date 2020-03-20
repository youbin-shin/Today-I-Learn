# HTML Review 및 개발환경

2020.03.09

> **학습 가이드라인**
>
> HTML 요소 참고서 : MDN (책보다 이 문서로 공부 추천)
>
> https://developer.mozilla.org/ko/docs/Web/HTML/Element
>
> HTML 콘텐츠 카테고리
>
> https://developer.mozilla.org/ko/docs/Web/Guide/HTML/Content_categories

### HTML5 & JavaScript

#### 웹 커리큘럼 안내

Static web : HTML, JS, CSS

Dynamic web with framework : django

SPA with fronted framework : v

#### 개발 환경 설정

##### Visual Studio Code

##### Chrome 개발자 도구

[ 주요 기능 ]

Elements - DOM 탐색 및 CSS 확인 및 변경

- Styles - 요소에 적용된 CSS 확인
- Computed - 스타일에 계산된 최종 결과
- Event Listeners - 해당 요소에 적용된 이벤트 (JS)

Console - JS 학습시 주로 사용

---

### 1차시 HTML5의 이해

> - HTML의 역사 및 표준체계
>   - 웹 표준, 브라우저 전쟁
> - HTML5의 특징 및 기본 구조
>   - 기본 구조
>   - Doctype, head, body

#### 현재의 웹 표준

대통합

#### HTML이란?

Hyper Text Markup Language : 웹페이지를 작성하기 위해 구조를 잡아주는 언어

- Hyper Text : 각 문서 내부마다 다른 문서에 연결되는 링크를 모두 다 가지고 있는 형태

  하이퍼텍스트를 주고 받는 규칙 : HTTP (Hyper Text Transfer Protocol)

- Markup : 문서의 구조를 잡는 것

  큰 제목, 작은제목, 목차, 본문 등 읽기 편하도록 크기와 문단을 지정해주는 것

웹용 콘텐츠의 구조를 지정하는 컴퓨터 언어

HTML은 **웹 페이지의 구조를 잡기 위한 언어**★

#### HTML 기본 구조

```html
<!DOCTYPE html> // 문서 타입 선언
<html lang="ko">
    <head> 
        <meta charset="UTF-8">
        <titile>Document</titile>
    </head>
    <body>
               
    </body>
</html>
```

DOM(Document Object Model) 트리

##### 요소(element)

```html
<h1>contents</h1> // 태그 꼭 닫아주기
<img src="url"/> // 닫는 태그가 없는 / 셀프 클로징 태그!
```

##### 속성(Attribute)

```html
<a href="https://google.com"></a>
```

href : 속성명

google.com : 속성값

속성과 속성값사이에 공백 NO!, "" 사용 권장

##### head

문서 제목, 문자 인코딩 등 문서 정보

메타데이터를 통해 웹 문서에 대한 추가 정보 선언

외부 파일 연결 - CSS 파일 혹은 JavaScript 파일

##### 메타 데이터를 표현하는 새로운 규약, Open Graph Protocol ★

HTML 문서의 메타 데이터를 통해 문서의 정보 전달

페이스북에서 만들었으며, 메타 정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

##### 시맨틱 태그 ★

HTML5에서 의미론적 요소를 담은 태그의 등장 ~~div~~

개발자 및 사용자 뿐 아니라 검색 엔진 등에 의미 있는 정보의 그룹을 태그로 표현

단순히 구역 나누기 X --> 의미를 가지는 태그들을 활용하기 위한 노력

Non semantic 요소 : div, span

검색엔진최적화(SEO) 를 위하여는 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 해야 한다.

[ 대표적인 태그 ]

- header : 문서 전체나 섹션의 헤더(머릿말 부분)
- nav : 네비게이션
- aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
- section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
- article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
- footer : 문서 전체나 섹션의 푸터(마지막 부분)

#### 웹사이트 분석하기 - web developer

설치 : 크롭 웹 스토어에서 "Web Developer" 검색 및 추가

---

### 2차시 HTML5 문서 구조화(상)

> - 블록 레벨 요소 / 인라인 레벨 요소
> - 섹션 요소 / 그룹 컨텐츠 요소
> - 전역 속성 (id, class, title)

#### 인라인 / 블록 요소

inline 속성 : 이미지, span, ...

CSS에서 자세히 다룰 예정

#### 그룹 컨텐츠

- `<p>`
- `<hr>`
- 목록 `<ol>`, `<ul>`
- `<pre>`, `<blockquote>` 인용문
- `<figure>`, `<div>`

#### 텍스트 관련 요소

- `<a>`

- `<b>` vs `<strong>`

  동일하게 동작하듯 보이지만 strong 강조 의미 +

  `<b>` 사용 X

- `<i>` vs `<em>`

  동일하게 동작하듯 보이지만 em 강조 의미 +

  `<i>` 사용 X

- `<span>`, `<br>`, `<img>`

- 기타 등등

---

### 3차시 HTML5 문서 구조화(하)

> - Table
> - Form
> - HTML5 기타 요소들
>   - ~~HTML5 새로운 form 요소, input 요소~~
>   - ~~HTML5 새로운 텍스트 요소들, HTML5 사라진 요소들~~

#### table

※ 이러한 내용이 있다 정도로 보기

- `<tr>` table row, `<td>` table data, `<th>` table head

- `<thead>`, `<tbody>`, `<tfoot>`

  tfoot은 마지막이 아닌 thead 밑에 두어도 마지막에 보인다.

- `<caption>`

- 셀 병합 속성 : `<colspan>`, `<rowspan>`

- scope 속성

- `<col>`, `<colgroup>`

```html
// 예시 코드
<body>
    <table>
        <thead>
            <tr>
                <th>이름</th>
                <td> 수학 점수</td>
            </tr>
        </thead>
        <tfoot>
            <tr>
                <td>계</td>
                <td>180</td>
            </tr>
        </tfoot>
        <tbody>
            <tr>
                <td>홍길동</td>
                <td>100</td>
            </tr>
            <tr>
                <td>길동이</td>
                <td>80</td>
            </tr>
        </tbody>
    </table>
</body>
```

#### form

※ 잔고나 직접 웹 사이트 만들 때 사용할 것이기에 중점적으로 보기

서버에서 처리될 데이터를 제공하는 역할

ex) 로그인할 때 아이디, 비번 입력과 같이 사용자에게 값을 받을 때 

[ 기본 속성 ]

- action
- method

---

# CSS Review

2020.03.10

### 4차시 CSS 문서표현(상)

> - CSS의 이해
>   - CSS 정의 방법, 선택자, 속성 선언
>   - 의사 클래스(pseudo class)
>   - 미디어쿼리
>   - 상속 및 우선 순위(이러닝 오류 있음)

#### CSS

CSS : Cascading Style Sheets, 스타일 정의 (HTML : 문서의 구조화 Markup)

- 기본 사용법 

  `selector{property:value; property:value; }`

  ex) h1 {color:blue; font-size:15px;}

- 정의 방법

  - 인라인 : 해당 태그에 직접 style 속성을 활용
  - 내부 참조 : HTML 파일 내에 `<style>` 태그에 지정
  - 외부 참조 ★ :  외부 CSS 파일을 `<head>` 내  `<link>`를 통해 불러오기

#### CSS Selector

선택자 : HTML 문서에서 **특정한 요소를 선택**하여 스타일링 하기 위해서 반드시 필요

- 기초 선택자
- 고급 선택자
  - 자손 선택자, 직계 자손 선택자
  - 형제, 인접 형제 선택자, 전체 선택자
- 의사 클래스 (있다 정도만 알기)
  - ~~링크, 동적 의사 클래스~~
  - ~~구조적 의사 클래스~~
  - ~~기타 의사 클래스, 의사 엘리먼트, 속성 선택자~~

```css
#sect1> ul> li:nth-child(1)
// # : id (id: 문서에서 1개만 쓴다)
// ul 안에 li 중에 1번째를 선택
```

##### CSS 상속 ★

CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다. 

- 속성(프로퍼티) 중에서 상속이 되는 것과 되지 않은 것들이 있다.

  - 상속 O

    ex) Text 관련 요소(font, color, text-align), opacity, visibility 등

  - 상속 X

    ex) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등

##### CSS 적용 우선 순위 (cascading order) ★

1. 중요도 importance

2. 우선 순위 Specificity

   인라인 / id 선택자 / class 선택자 / 요소 선택자

3. 소스 코드 선언 순서

##### CSS 우선 순위 Quiz

```html
<p>1</p> // green
<p class="blue">2</p> // blue
<p class="blue skyblue">3</p> // ★ skyblue
<p class="skyblue blue">4</p> // ★ skyblue
<p id="red" class="blue">5</p> // red
<h3 id="red" class="blue">6</h3> // violet (h3에 important 있기에)
<p id="red" class="blue" style="color: yellow";>7</p> // yellow
<h3 id="red" class="blue" style="color: yellow";>8</h3> // violet
```

```css
h3 {color: violet_!important}
p {color: green;}
.blue {color: blue;}
.skyblue {color: skyblue;}
#red {color: red;}
```

3, 4 같은 경우 소스 코드 자체의 순서를 통해 결정되는데 나중에 선언된 것이 더 우선하여 skyblue의 색을 띄게 된다.

---

### 5차시 CSS 문서표현(하)

> - 텍스트의 표현
>   - 폰트 패밀리, 크기 단위, 변형 서체(~~<b>, <i>~~ vs <strong>, <em>)
>   - ~~자간 , 단어 간격, 행간, 들여쓰기~~
>   - ~~기타 꾸미기~~
> - 컬러와 배경(backgroung-image, background-color) ---> 있다 정도로 알고 있기
> - 목록꾸미기
> - ~~표 꾸미기~~
> - CSS 박스 모델
> - Position

#### 기초 CSS

##### 크기 단위 (상대)

- px (브라우저에서 기본 16px)

- %

- em : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐, 갖을 수 있는 사이즈에 곱해지기에 상대적인 값

  - rem과의 차이 : rem 최상위 태그의 font-size 기준, em은 현재 요소의 font-size 기준 

  ```css
  html {font-size: 16px;}
  body {font-size: 2em;}
  div.container {font-size: 2rem;}
  div.content1 {font-size: 2rem;} // font-size : 32px
  div.content2 {font-size: 2em;} // font-size : 16*2*2*2 = 128px
  ```

- rem : root em, 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐., 어디에 적용되도 같은 값

  - ex) html 태그의 font-size값이 16px이라면 2rem = 32px, 1.5rem = 24px, 1.25rem = 20px

- Viewport 기준 단위

  vw, vh, vmin, vmax

  - vh : 브라우저 높이를 기준으로

  - vw : 브라우저 너비를 기준으로

  - - 예) 10vh -> 전체 높이의 크기의 10%

  - vmin : 높이/너비 중에 작은 것 기준으로

  - vmax : 높이/너비 중에 높은 것 기준으로

  - - 예) 높이 720px, 너비 1080px 일때, 10vmin이면, 72px

  일부 익스플로워에서 적용이 안되는 경우가 있다 정도 알고 가기

##### 색상 단위

- HEX(00~ff) : #fffff
- RGB(0, 255) : rgb(0, 0, 0)
- RGBA : rgba(0, 0, 0, 0, 5)

#### Box model ★

- Content : 실제 내용이 위치

- Padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경의 컬러/이미지는 패딩까지 적용

- Border : 테두리 영역

- Margin : 테두리 바깥의 외부 여백 배경색을 지정 X

  - 마진 상쇄 (Margin collapsing)

    인접 형제 요소 간(top, bottom이 같이 주어지는 경우)의 margin이 겹쳐서 보임

![boxmodel img](https://user-images.githubusercontent.com/60081201/76813512-91669600-683b-11ea-97ec-3b3dc2745017.JPG)

![margin im](https://user-images.githubusercontent.com/60081201/76813530-a0e5df00-683b-11ea-8d51-89b002160b35.JPG)

※ margin-3 { margin: 10px auto 30px; } // 좌우 같은 margin, 가운데 정렬

- box-sizing

  - 기본적으로 모든 요소의 box-sizing : content-box
    - padding 을 제외한 순수 contents 영역만을 box로 지정
  - 다만, 우리가 일반적으로 영역을 볼 때는 border 까지의 너비를 100px 보는 것을 원함.
    - 이 경우에 box-sizing★을 **border-box**

  ![quiz img](https://user-images.githubusercontent.com/60081201/76813549-b0fdbe80-683b-11ea-82ae-7fcbc60feb46.JPG)

#### Display 속성 ★★(inline, block 구분 시험각)

이외에도 다양한 display가 있지만 지금은 이것만 기억하자!

- display: block

  - **줄 바꿈 일어나는 요소**

  - **화면 크기 전체의 가로폭을 차지**

    - width = 100px로 하면 나머지 부분들은 자동으로 margin을 준다! ★

  - 블록 레벨 요소 안에 인라인 레벨 요소 들어갈 수 있음

  - 대표적인 블록 레벨 요소

    div/ ul, ol, li/ p/ hr/ form 등

- display: inline

  - **줄 바꿈이 일어나지 않는 행의 일부 요소**

  - **content 너비만큼 가로폭을 차지**

  - **width, height, margin-top, margin-bottom 지정 X**

  - 상하여백은 line-heignt로 지정

  - 대표적인 인라인 레벨 요소

    span/ a/ img / input, label/ b, em, i, strong 등

- display: inline-block

  - block, inline 레벨 요소의 특징 모두 갖는다.
  - inline 처럼 한줄에 표시 가능
  - **block 처럼 width, heignt, margin 속성 모두 지정 가능**

![blockinline](https://user-images.githubusercontent.com/60081201/76827411-149ae280-6862-11ea-9c55-e9e5ad3d973c.JPG)

- 속성에 다른 수평 정렬

  |                            블록                            |       인라인        |
  | :--------------------------------------------------------: | :-----------------: |
  |                    margin-right: auto;                     |  text-align: left;  |
  |                     margin-left: auto;                     | text-align: right;  |
  | margin-rignt: auto; margin-left: auto; <br />--> 수평 정렬 | text-align: center; |

---

# 레이아웃과 고급 CSS Review

2020.03.11

### 6차시 레이아웃과 고급 CSS 기능

> - **다단 레이아웃** ★
>   - **position**
>   - **display**
>   - **float**
> - 네비게이션
>   - ~~이미지 버튼~~
>   - ~~텍스트 네비게이션(추후 실습에 포함)~~
> - ~~animation, transition~~
>   - ~~요소의 변형~~
>   - ~~요소 클리핑~~

#### CSS position

- static : 디폴트 값 (기준 위치)

  - **기본적인 요소의 배치 순서에 따름 (좌측 상단)**
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치

- property(top, bottom, left, right) 사용하여 이동 가능 (음수값도 가능)

  - relative 상대 위치 : static 위치를 기준으로 이동

    ```css
    .relative {
        position: relative; 
        top: 100px; // 위를 기준으로 100px 밑으로
        left: 100px; // 왼쪽을 기준으로 100px 오른쪽으로 이동한 위치
    }
    ```

  - absolute 절대 위치 : **static이 아닌 ★** 가장 가까이 있는 **부모/조상 요소를 기준**으로 이동

    ※ 사용시 조심하기 --> 본인의 위치을 없애기 때문에

    ```css
    .parent {
        position: relative; // static이 아닌 것을 기준으로 하기에 반듯이!!!필요
    }
    
    .absolute-child {
        position: absolute; // 부모 요소 기준으로 50 밑으로 50 오른쪽으로 이동
        top: 50px;
        left: 50px;
    }
    ```

    ![re vs ab 차이](https://user-images.githubusercontent.com/60081201/76827441-28dedf80-6862-11ea-8223-0e628c8a3ade.JPG)

    위의 그림 : **absolute vs relative 차이**

    absolute는 원래 있어야하는 위치를 지워 동생이라는 네모칸이 기본 정렬(좌상)으로 이동한 것이고 relative는 자신이 원래있던 위치는 기둥을 세워둔 것처럼 빈공간으로 인식되지 않는다. 따라서 absolute 같은 경우에 본인의 원래 위치를 없애버리기에 레이아웃이 다 깨질 수 있음!! 따라서 사용을 주의해야 한다!!

  - fixed 절대 위치 : 부모 요소와 관계 없이 브라우저를 기준으로 이동

    - 스크롤시에도 항상 같은 곳에 위치

    ```css
    .fixed {
        position: fixed;
        bottom: 0;
        right: 0;
    }
    ```

#### CSS float

[ 속성 ]

- Float는 요소를 <u>일반적인 흐름 (normatl flow)</u> 에서 벗어나도록 하는 속성 중 하나
  - 일반적인 흐름 : 박스모델, 좌상으로 배치
  - 반드시 ★clear 속성을 통해 **초기화가 필요**하며 예상치 못한 상황 발생할 수 있음.
  - 둥둥떠있다고 생각하기(입체적! 위에 글씨 안써짐) --> 배치 흐름을 바꿔버림 --> clear 필요
  - middle 속성 X 오직 left 또는 right
- float를 사용하는 경우 block 사용을 뜻하며, display 값이 inline인 경우에도 block으로 계산된다.

[문제점 & 해결안]

- Float가 발생시키는 문제

  - 자식 요소의 float 속성으로 인해 부모 영역의 높이가 사라지는 문제
  - clear 한 요소의 margin이 제대로 표현이 되지 않는 문제

- 해결방안

  - 다양한 방안 존재하지만 가장 많이 활용되고 문제가 없는 의사(가상) 요소 선택자를 활용한 방법

  ```css
  .clearfix::after {
      content: "";
      display: block;
      clear: both;
  } // 비어있는 내용으로 block을 만들고 그걸 clear 
  ```

  after 선택자 : 요소의 다음에 content 내용을 담아줌

#### CSS Layout

##### HTML/CSS의 기본 특징 ★

- 일반적으로 HTML 요소들은 문서의 **위에서부터 아래로** 순차적을 나열
- 아래의 방법을 통해 변경 가능
  - display 속성을 통해 요소가 보여지는 (표현되는) 방식 변경
    - block, inline, inline-block
    - table, flexible box, grid 등의 레이아웃을 활용
  - position 속성을 통해 위치 자체를 변경 --> **absolute** : 본인공간 X
  - **float** 속성을 통해 떠있도록 만듦

##### CSS를 어렵게 만드는 요소

- 일반적인 흐름 (Normal flow)을 바꿔버리는 경우
- Normal flow : inline, block, relative, position
- **Floats**
- **Absolute positioning**  --> 네모위에 네모가 싸이거나 네모사이에 아이콘 있는 경우들은 무조건 absolute positioning 에 의해 만들어진 것!!

---

# 자바스크립트 Review

2020.03.12

### 7차시, 8차시 자바스크립트 기초 및 문법

> - JavaScript 구문
> - 데이터 타입 및 변수
> - 연산자
> - 조건/반복문
>
> JavaScript 읽을 수 있을 정도로 알면 된다.
>
> 자바스크립트 암기형 평가 진행 X, 강의에 언급한 차이점정도만 기억하기

#### JavaScript

##### 브라우저에서 할 수 있는 일

- 전역 객체 window
  - DOM 조작
  - BOM 조작
    - navigator, screen, location, frames, history, XHR
  - JavaScript
    - Object, Array, Function

#### JavaScript 기초

##### 변수 선언

- 변수 선언은 `var` 키워드를 활용해야 함
- ES6 기준으로 `const`, `let` 키워드 등장함

##### 데이터 타입 분류 (typeof)

- 원시 타입(primitive) - 변경 불가능한 값(immutable)

  - boolen - true, false
  - null
  - undefined
  - number
  - string
  - symbol (ES6)

- 객체 타입(Object)

  - object : 일반 객체, function, array, date, RegExp

  ```javascript
  // 형변환
  > String(19)
  "19"
  > Boolean(0)
  false
  > Number('123')
  123
  ```

##### Number

- 모든 숫자는 number 타입

- 8진수 (0), 16진수(0x)로 표현 가능

- 추가적으로 Infinity, -Infinity, **NaN**(not a number)도 number 타입

  ```javascript
  > typeof NaN
  "number"
  > typeof Infinity
  "number"
  > typeof -Infinity
  "number"
  ```

- 정수의 타입이 별도로 없는 것이지 정수라는 수체계가 존재하지 않은 것은 아니다.

- IEEE 754 표준에 따라서 부동 소숫점으로 표현되며, -2^53~2^53의 정수만 안전하게 표현 가능하다.

  ```javascript
  > Math.pow(2, 53)
  9007199254740992
  > Math.pow(2, 53) + 1 // 더해지지 않음
  9007199254740992
  > Math.pow(2, 53) * 2
  18014398509481984
  > Number.isSafeInteger(Math.pow(2, 53)-1)
  flase
  > Number.isSafeInteger(Math.pow(2, 53)-1)
  true
  ```

##### String - 템플릿 문자열(ES6)

- 편하게 문자열 내에 변수를 사용(string interpolation) 사용

- 여러 라인으로 이뤄진 문자열 사용 가능

  ```javascript
  > var name = 'kim'
  > console.log('Welcome to live session, Mr. ${name}!')
  Welcome to live session, Mr. kim! // 파이썬 f-sting과 비슷
  ```

##### null vs undefined

- null

  - 의도적으로 변수에 값이 없다는 것을 명시
  - typeof 출력시 object로 출력되는 것은 설계상의 실수

- undefined

  - 선언 이후 할당하지 않은 변수에 지정된 값

    ex) var a 이렇게 선언할 때 값을 할당되지 않고  자동적으로 초기화된 값이 undefined!!

    ```javascript
    > var a
    undefined
    ```

  - 자바스크립트 엔진이 할당 이전에 초기화된 값

  - 직접 값으로 할당해서 사용하는 것 금지

##### 객체

- 자바스크립트는 원시 타입(primitive type)을 제외하고는 모두 객체이다.

- 자바스크립트의 객체는 **키(문자열/심볼)**와 **값**으로 구성된 속성(property)의 집합이며, 프로퍼티 값이 함수일 경우 구분을 위해 메소드라고 부른다.

  ```javascript
  > var person = {
      name: 'hong';
      greeting: function() {
          console.log('Hi, I am ${this.name}')
      } // 값이 함수일 때 메소드라고 부름
  }
  
  > person.greeting()
  Hi, I am hong
  ```

##### Array

- 배열은 대괄호를 통해 만든다.

  ```javascript
  > var a = [1, 2, 3, 'hi']
  > console.log(a)
   > (4) [1, 2, 3, 'hi']
  > var b = new Array()
  > b[0] = 1
  1
  > console.log(b)
   > [1]
  > typeof b
  "object"
  ```

##### 함수

- 함수 선언 두가지 방법

  ```javascript
  // 1
  // 선언할 때 이름 add를 써서 하는 방법
  function add(num1, num2) {
      return num1 + num2;
  }
  
  // 2
  // 함수 이름 없이 만들어서 변수에 저장하여 사용하는 방법
  const sub = function(num1, num2) {
      return num1 - num2;
  }
  ```

##### 변수 유효 범위 scope

- 자바스크립트는 함수 레벨 스코프를 가진다.
- **함수 내에서 선언된 변수는 지역 변수**이며, 나머지는 전역 변수로 활용된다.
- 변수 선언시 키워드`var`를 쓰지 않으면, 암묵적 전역으로 설정된다. --> **변수 선언시 키워드 `var`을 써야 한다.**
  - 주의 : 변수가 아닌 전역객체(window)의 프로퍼티로 생성
  - 따라서, delete(객체의 속성을 지우는 연산자)로 지워지는 값

##### 호이스팅과 elt, const(ES6)

- 자바스크립트에서는 모든 선언을 **호이스팅** 한다.

  --> 함수 사용하는 코드 뒤에 함수가 선언되어 있어도 괜찮음!  호이스팅은 적용 X, 존재 자체를 알면 된다.

- ES6에서 새롭게 등장한 <u>let과 const 키워드</u>는 이러한 <u>내용 방지</u> 가능 --> 방지하는 키워드가 존재한다 정도 알면 된다.

  - 호이스팅 자체가 이뤄지지 않는 것은 아니고 var는 선언과 동시에 초기화(undefined)를 하고, let, const는 선언과 초기화 단계가 분리되어 진행된다.
  - 또한 블록 레벨 스코프를 가지고 있으며 이는 나중에 다룰 예정

##### 호이스팅에 대한 설명 plus

- 함수 선언식 (var 처럼 동작)

  ```javascript
  add(1, 2) // 3
  function add(num1, num2) {
      return num1 + num2
  }
  ```

- 함수 표현식(호이스팅 시 에러)

  ```javascript
  sub(7, 2) // Uncaught ReferenceError: Cannot access 'sub' before initialization
  const sub = function(num1, num2) {
      return num1 - num2
  }
  ```

  - 이는 함수를 변수에 할당함으로 변수로 평가되어 변수의 scope 규칙을 따르기 때문
  - 그런데 함수 표현식을 var 로 선언한 경우 다른 에러가 발생합니다.

  ```javascript
  sub(1, 2) // Uncaught TypeError: sub is not a function
  var sub = function(num1, num2) {
      return num1 - num2
  }
  ```
  - 변수가 선언하기 전 undefined 로 초기화 되어 위 const 예시와 에러 메세지가 다름

#### JavaScript 문법

##### 연산자

값일치를 비교하려면 === 이용하기!

== vs === ★ 

- == 동등 연산자 : 값 비교 및 예상치 않은 변환

- === 일치 연산자 : 엄격한 같음, 형 비교

  ```javascript
  > 0 == ''
  true
  > 0 =='0'
  true
  > '' =='0'
  false
  ```

##### 조건문

파이썬과 차이점

1. elif (python) --> else if
2. if : --> if {} 

##### 반복문

```javascript
// for 문
for (let j=0; j < 10; j++) {
    console.log(j)
}

// while 문
let i = 0
while (i < 10) {
    console.log(i);
    i++;
}
```

---

### 9차시 내장 객체

> - 객체의 이해와 생성
> - 내장 객체
>   - ~~Number~~
>   - ~~String~~
>   - ~~Date~~
>   - ~~Math~~
>   - ~~RegExp~~

보기만 하기! 암기할 필요 X, 내장 객체 있다 정도만 알고 있기

---

# 자바스크립트 함수 Review

2020.03.13

### 10차시 배열과 함수

> - 배열
> - 함수

#### JavaScript Object

##### 객체(Object) 생성 방법

- 객체는 **Key**와 **Value**로 구성된 속성(property)들의 모임

- 기본 객체 생성법

  - 객체 리터럴

    - 키가 문자열로 표기될 수 있다면, 암묵적 형변환 발생
    - 그게 아닌 경우는 반드시 따옴표를 통해 문자열(ex. e-mail)로 만들어 주어야 한다.

    ```javascript
    var cat = {name: 'nero', age: 3, 'e-mail':'cat@com'}
    ```

  - Object 생성자 함수

    - 마치 클래스 처럼 속성이 동일한 객체 생성 가능

    ```javascript
    var dog = new Object()
    dog.name = 'kitek'
    dog.age = 9
    > dog
    {name: 'kitek', age: 9}
    ```

##### 객체 속성 접근

`.` 혹은 `[]`로 접근 가능

단, 반드시 []로 접근(key가 스트링이 아닌 경우 ex) cat['e-mail'])을 해야하는 경우가 있다.

#### 배열 Array

- JS에서 배열은 값만 존재한다.

##### 배열 생성 방법

- 배열 리터럴

  ```javascript
  var a = [1, 2, 3]
  ```

- Array 생성자 함수

  ```javascript
  var b = new Array(1, 2, 3)
  ```

##### 배열 순회

1. for

2. for ... of

3. forEach

   ```javascript
   // 1. for
   var a = [1, 2, 3]
   for (var i = 0; i < a.length; i++) {
       console.log(i, a[i])
   } // 출력: 0 1/ 1 2/ 2 3
   
   // 2. for ... of
   for (var elem of a) {
       console.log(elem)
   } // 출력: 1/ 2/ 3
   
   // 3. forEach --> 인자로 함수자체를 받음
   a.forEach(function(elem, idx) {
       console.log(idx,elem)
   }) // 출력: 0 1/ 1 2/ 2 3
   ```

4. for ... in

   > for in 보다는 앞에 말한 3가지 사용을 추천

   배열의 요소만 접근하는 것이 아니라 속성까지 출력될 수 있다.

   자바스크립트에서 배열도 object라서 속성 설정이 가능하지만, 리스트의 요소가 아니라, 객체의 속성이 된다.

   ```javascript
   a.name = 'myarr' --> a = [1, 2, 3, name:"myarr"]
   for (var i in a){
       console.log(i, a[i])
   } // 출력: 0 1/ 1 2/ 2 3/ name myarr
   
   ```

##### 배열 메소드

> 각자 메소드 어떤 역할을 하는지 알기, splice vs slice 차이★

- 정렬 메소드

  - sort 메소드에 비교 함수(인자)가 없으면 <u>문자열 기준으로 정렬</u>한다.
  - 비교함수가 있다면, 해당 함수의 리턴값이 0보다 크거나 작음을 정렬한다.

  ```javascript
  // sort 메소드 사용하여 정렬하기
  var numbers = [4, 3, 2, 5, 1, 100];
  numbers.sort();
  console.log(numbers);
  // 출력:(6) [1, 100, 2, 3, 4, 5]
  
  // sort 메소드 + 비교함수 이용하여 정렬하기
  var numbers = [4, 3, 2, 5, 1, 100];
  numbers.sort(function(a, b){ // 비교함수★
      return a-b
  });
  console.log(numbers);
  // 출력: (6) [1, 2, 3, 4, 5, 100]
  ```

- 문자열 관련 - join, toString

  ```javascript
  var a = [1, 2, 3]
  a.join('-') // 출력: "1-2-3"
  a.toString() // 출력: "1, 2, 3"
  ```

- 배열 합치기 - concat

  ```javascript
  var a = [1, 2, 3]
  a.concat([4, 5]) // 출력: (5) [1, 2, 3, 4, 5]
  
  a + [4, 5] // python 처럼 시행하면 X
  // 출력: "1, 2, 34, 5"
  ```

- 원소 삽입/삭제 - push, pop, unshift, shift

  - push/pop : 배열 뒤에 넣기/빼기
  - unshift/shift : 가장 처음에 인덱스에 넣기/빼기

  ```javascript
  var a = [1, 2, 3]
  a.push(4) // 출력: 4
  a.pop() // 출력: 4
  a.unshift(0) // 출력: 4
  a // 출력: (4) [0, 1, 2, 3]
  a.shift(0) // 출력: 0
  a // 출력: (3) [1, 2, 3]
  ```

- 인덱스 탐색 - indexOf

  어떠한 원소가 어떤 index를 가지는 지 확인 가능

  ```javascript
  var a = [1, 2, 3]
  a.indexOf(3) // 출력: 2
  a.indexOf(5) // 출력: -1
  ```

- 배열 조작 - splice & 배열 자르기 - slice

  > 차이 알아두기

  - **splice** : 원본 배열을 바꿔줌, 원소의 삭제/수정 가능
  - **slice** : return 해줌

  ```javascript
  // splice 사용
  var a = [1, 2, 3]
  a.splice(1) // 출력: (2) [2, 3]
  a // 출력: [1]
  
  // slice 사용
  var a = [1, 2, 3]
  a.slice(-2) // 출력: (2) [2, 3]
  a.slice(1, 2) // 출력: [2]
  a.slice(1) // 출력: (2) [2, 3]
  a.slice() // 출력: (3) [1, 2, 3]
  
  
  // splice 원소 삭제/수정 예제
  // splice(배열의 변경을 시작할 idex, 삭제할 원소의 개수, 추가할 값들)
  var a = [1, 2, 3]
  a.splice(1, 2, '처음', '두번') // 출력: (2) [2, 3]
  a  // 출력: (3) [1, "처음", "두번"]
  var a = [1, 2, 3]
  a.splice(1, 2, '처음') // 출력: (2) [2, 3]
  a // 출력: (2) [1, "처음"]
  ```

#### 함수 ★

##### 함수 만들기

- **함수 선언문** : 함수 이름과 함께 작성

- **함수 표현식** : 변수에 익명 함수를 넣어서 사용

- 즉시 실행 함수

  ```javascript
  // 함수 선언문
  function sum(a, b) {
      return a + b;
  }
  sum(1, 2) // 출력: 3
  
  // 함수 표현식
  var sub = function(a, b) {
      return a - b;
  }
  sub(1, 2) // 출력: -1
  
  // 즉시 실행 함수
  (function(a, b) {return a * b})(1, 2) // 출력: 2
  ```

- 화살표 함수

  > 후반부 수업(뷰)에서 실제로 많이 사용할 예정

  ```javascript
  var sum = (a, b) => a + b
  sum(3, 4) // 출력: 7
  
  
  var area = (r) => {
      const PI = 3.14;
      return r * r * PI;
  }
  area(1) // 출력: 3.14
  ```

##### 함수 인자

- 자바스크립트에서 함수는 매개변수 전달에 대한 제한이 없음

  어떠한 인자 정의되어 있지 않으면 undefined

- arguments 객체는 매개변수로 넘겨진 모든 정보를 가지고 있음

---

# DOM 및 이벤트 Review

2020.03.16

### 11차시 문서 객체 모델 (DOM)

> - window 객체
> - DOM 접근
> - DOM 조작
>   - 노드의 생성과 삽입, 조작
>   - 노드에 CSS 속성 적용
>   - innerHTML

#### DOM (Document Object Model)

##### DOM

- 문서의 **구조화된 표현을 제공**하여, DOM 구조에 접근할 수 있는 방법을 제공

- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 도우며, 구조화된 노드와 오브젝트로 문서를 표현 

- 주요 객체 ★

  - **window** : DOM 문서를 표현하는 창, 가장 최상위 객체
  - **document** : 페이지 콘텐츠의 진입점 역할을 하며 `<body>` 등 다른 요소들을 표함
  - navigator, location, history, screen

  ```javascript
  window.screen.heignt  // 출력: 2160
  document.title // 출력: "Sign up GitLab"
  history.back() // 뒤로가기 버튼과 같은 동작 실행
  ```

##### window

- window 객체는 전역 객체

- 다양한 함수, 이름 공간, 객체 등이 포함

- 개발자 도구에서 console > window에 들어가면 무수히 많은 값, 메서드 갖고 있음

  ```javascript
  var test = 'test'
  window.test // 출력: "test" --> 이름공간을 가짐
  ```

#### DOM 조작

##### DOM 접근

> ★ 있는 두가지만 기억하자
>
> 나머지는 있다 정도로 알고 있기

- 단일 Node

  - document.getElementByID(id)
  - **document.querySelector(selector)** ★

- HTMLCollection(live)

  live collection이기에 반복문이나 조건문 수행시 변경된 내용이 실시간으로 바뀌기 때문에  활용시 주의하기

  - document.getElementsByTagName(class)
  - document.getElementsByClassName(class)

- NodeList(non-live)

  NodeList는 경우에 따라 live collection 일 수 있다. 하지만 밑에 있는 querySelectorAll은  non-live!

  - **document.querySelectorAll(selector)** ★

  ※ 참고 : selector에는 `#id`, `.class`, `tagName` 넣어주면 된다.

##### DOM Node 기준 탐색

> 노드를 찾아갈 수 있음을 알고 나중에 찾아 쓸 수 있을 정도로 알고 있기

- parentNode, firstChild, lastChild
- Element
  - children
  - previousElementSibling, nextElementSibling
- 모든 요소
  - childNodes
  - prevSibling, nextSibling

##### Node 생성

> 이것도 이러한 방식들이 있다 정도로 기억하기

- document.createElement(tagName) : 특정 태그를 생성
- document.createTextNode(text) : 텍스트 노드를 생성
- parentNode.appendChild(Node) : 마지막 자식 요소로 추가
- parentNode.removeChild(Node) : 해당 요소를 제거

##### innerHTML, insertAdjacentHTML 메소드

> 보안 취약점이 있지만 이두가지 기억하기 이를 이용하여 편하게 조작하자

- DOM 조작시 아래와 같은 메서드를 통해서도 가능하다 XSS 공격에 취약점이 있으므로 사용시 주의.

- element.innerHTML(text)

- element.insertAdjacentHTML(position, text)

  - position: beforebegin, afterbegin, beforeend, afterend

    ```html
    // beforebegin
    <ul>
        // afterbegin
        <li></li>
        //beforeend
    </ul>
    //afterend
    --> 위치 지정 가능
    ```

##### Node attribute

> attribute를 통해 속성값 바꿔줄 수 있다 기억하기

- element.style
  - element.style.color
  - element.style.backgroundColor
- element.setAttribute(attributeName, value)
- element.getAttribute(attributeName)



> 11차시 기억해야할 것은 DOM 조작을 할 수 있는 메소드들이 있다. 그 메소드들은 document를 기준으로 혹은 element를 기준으로 각각 존재하는데 그 내용들을 잘 정리하면 된다.
>
> DOM을 기준으로 하나를 갖고 오고 싶은 때 querySelector 혹은 querySelectorAll 두가지 방식 중에 하나로 활용하면 된다.

#### 브라우저에서 할 수 있는 일

- DOM(Document Object Model) 조작

  (DOM: 문에 대한 모든 내용을 담고 있는 객체, 도큐먼트에 관련된 내용 모두, 열려진 페이지에 대한 정보에 따라 객체화시켜서 관리)

- BOM(Brouser Object Model) 조작

  (BOM: 브라우저에 대한 모든 내용을 담고있는 객체, 브라우저에 관련된 내용 모두, 뒤로가기/북마크/즐겨찾기/히스토리/URL 정보 등)

  - navigator, screen, location, frames, history, XHR

- JavaScript

  - Object, Array, Function

---

### 12차시 이벤트

> - 이벤트
> - 이벤트 전파

#### JavaScript Event

##### Event

- 브라우저에서 특정한 이벤트가 발생하면 이에 대한 이후 행위 정의 가능함
- 이벤트를 정의하는 경우, 인라인으로도 작성 가능하나 분리하여 작성하는 것이 좋다.
- 아래는 가능한 이벤트 예시이다.
  - load, copy, mouseover, click, submit 등

##### addEventListener

- EventTarget.addEventListener(type, listener, [, useCapture]);

  - type : 이벤트 유형
  - listener : 이벤트가 발생했을 때 실행할 콜백 함수(핸들러) --> 실행하고 싶은 함수
  - useCapture : 기본 값(false), 상위 노드로 전파(버블링), 만약 true인 경우 하위 노드로 전파(캡처링)

  ```javascript
  const button = document.querySelector('button');
  button.addEventListener('click', function() {
      console.log('click');
  })
  ```

  > 위와 같은 코드 안에 함수를 보는 것 익숙하도록 하기! 만드는 연습도 많이 필요하다.

##### 이벤트 전파

- Event는 해당 요소에서 전파되며, 캡처링과 버블링으로 구분된다.
- 항상 캡처링부터 시작하여 버블링으로 종료되며, addEventListener 메소드와 useCapture를 통해 특정 상황에 대하여 이벤트 관리가 가능하다.
  - capture 파트를 이용할지 bubbling 파트를 이용할지 결정하는 것이 addEventListener의 세번째 인자다.
    - 세번째 인자는 옵션, 기본값은 false --> bubbling
    - 세번째 인자에 true를 하면 captureing

![이벤트 전파](https://user-images.githubusercontent.com/60081201/76916842-1bc6fc80-6905-11ea-903c-39731e85bd74.JPG)

##### 이벤트 객체와 this

이벤트 리스너의 콜백함수에서 this를 활용하는 경우, 이벤트 리스너에 바인딩 되어 있는 요소가 지정된다. 아래와 같이 이벤트를 등록하는 경우 버블링에 의해 this 값은 계속 변경된다.

```html
<stript>
    const clickEvent = function(event) { // event 인자는 첫번째로 들어오는 값(이 코드에서는 event가 언제/어디서 발생했는지 볼 수 있음)
    console.log('target')
    console.log(event.target);
    console.log('current target')
    console.log(event.currentTarget);
    console.log('this')
    console.log(this);
    }
    const button = document.querySelector('button');
    button.addEventListener('click', clickEvent); // 세번째 인자 기본 false 이기에 bubbling!!
    // 따라서 button을 눌렀을 때 button -> div -> body 순으로 올라간다. -- 전파
    const div = document.querySelector('div');
    div.addEventListener('click', clickEvent);
    const body = document.querySelector('body');
    body.addEventListener('click', clickEvent);
</stript>
```

```html
// 개발자 도구 - console 화면
target
  <button>버튼</button>
current target
  <button>버튼</button>
this
  <button>버튼</button>
target
  <button>버튼</button>
current target
  <div></div>
this
  <div></div>
target
  <button>버튼</button>
current target
  <body></body>
this
  <body></body>

// --> target : 실질적으로 발생한 곳, current target : 전파되고 있는 노드를 보여줌, this : current target 과 동일한 값을 가짐
```

##### 이벤트 객체

- 이벤트에 지정된 함수(핸들러)는 이벤트 객체를 매개변수로 받을 수 있음
- 이벤트 객체의 대표적인 속성과 메소드
  - Event.target : 이벤트가 원래 발생하였던 대상
  - Event.currentTarget : 이벤트가 발생하였던 대상
  - Event.preventDefault() : 이벤트를 취소
  - Event.stopProgation() : 이벤트 전파 중단

---

# 함수 고급 기능 Review

2020.03.17

### 13차시 함수의 고급 기능

> - 함수의 고급 기능
>   - 함수 정의
>   - 클로저

#### 함수 호이스팅

> 주의해야하는 개념! 활용 X

- 자바스크립트에서는 모든 선언이 호이스팅 된다.

  > 변수 호이스팅 막기 위해 let, const 키워드가 있었다까지 기억하기

- 함수 선언문과 함수 표현식의 차이 ★

  - 함수 선언문의 경우 선언, 초기화, 할당이 모두 이뤄져 실행 가능
  - 함수 표현식은 변수 호이스팅이 발생하여(호출 X), undefined. 즉 실행불가
  - 일반적으로 함수 선언문 보다는 함수 표현식으로 작성하게 될 것이다.

  ```javascript
  // 함수 선언문
  console.log(sum(1, 2)) // 출력: 3
  function sum(a, b) {
      return a + b;
  }
  
  
  // 함수 표현식
  console.log(sub(1, 2)) // 출력: TypeError
  var sub = function(a, b) { // function 익명 함수
      return a - b;
  }
  ```

#### Array helper methods

- forEach : 주어진 함수를 배열의 요소 각각에 대해 실행

  구문 `arr.forEach(callback(currentvalus[, index[, array]])[, thisArg])`

  - callback : 각 요소에 대해 실질적으로 실행되는 함수
  - currentValue : 처리할 현재 요소
  - index (optional) : 처리할 현재 요소의 인덱스
  - array (optional) : forEach()를 호출한 배열
  - thisAry (optional) : callback을 실행할 때 this로 사용할 값

  ```javascript
  // 예제 눈여겨보기 ★
  const numbers = [1, 2, 3]
  numbers.forEach(function(elem, idx, arr) { //--> 함수 호출, 선언
      console.log(elem, idx, arr)
  })
  /* 출력 : 
  1 0 (3) [1, 2, 3]
  2 1 (3) [1, 2, 3]
  3 2 (3) [1, 2, 3]
  */
  ```

- filter : 주어진 함수를 배열의 요소 각각에 대해 실행하여 <u>반환값이 true 인 요소를 모아 배열로</u> 반환

- map : 주어진 함수를 배열의 요소 각각에 대해 실행한 <u>결과를 모아 배열</u>로 반환

- every : 주어진 함수에 모든 요소가 true인 경우 true (boolean 값 반환)

- some : 주어진 함수에 하나라도 true인 경우 true (boolean 값 반환)

- 이외에도 reduce, find 함수 등 존재

  ```javascript
  const images = [
      {heignt: 10, width: 30},
      {heignt: 20, width: 90}
  ]
  const areas = []
  images.forEach(function(image){
      areas.push(image.height * image.width)
  })
  areas // 출력: (2) [300, 1800]
  
  
  const numbers = [1, 2, 3]
  numbers.map(function(number){
      return number * 2
  }) // 출력: (3) [2, 4, 6]
  
  
  const products = [
      {name: 'cucumber', type: 'vegetable'},
      {name: 'banana', type: 'fruit'},
      {name: 'carrot', type: 'vegetable'},
      {name: 'apple', type: 'fruit'}
  ]
  products.filter(function(product){
      return product.type === 'fruit'
  })
  /* 출력:
  (2)
  0: {name: 'banana', type: 'fruit'}
  1: {name: 'apple', type: 'fruit'}
  */
  ```

#### JavaScript Closure

##### First class function 

- 자바스크립트 함수의 특징 ★

  > 특징 세가지 암기하기

  - 함수를 인자로 전달 가능
  - 함수를 반환 가능
  - 변수에 함수 할당 가능

- 위의 조건은 프로그래밍 언어에서의 일급 객체(first class object / first class citizen)의 조건이다.

  모든 원시타입은 일급 객체! 이때 함수도 가능하다가 핵심

```javascript
// 1. 함수를 인자로 전달
const numbers = [1, 2, 3]
numbers.map(function(number){ 
    return number * 2
}) // 출력: (3) [2, 4, 6]

// 2. 함수를 반환
function hello(){
    return function(){
        console.log('happy')
    }
}
hello()() // 출력: happy
var a = hello()
a() // 출력: happy
```

##### Closure ★

함수와 함수가 선언된 어휘적 환경(Lexical scoping, environment)의 조합

```javascript
function makeAdder(){
    var x = 1
    return function(y) {
        return x + y
    }
}

var add1 = makeAdder()
var add2 = makeAdder()
add1(1) // 출력: 2
add2(3) // 출력: 4
```

변수에 makeAdder() 하면 function(y) 부분만 저장되는 것이 아니라 어휘적 환경을 고려하여 x = 1도 저장되어 있어 return 값이 add1(1)에서 1+1이 나온다. 이 개념이 closure!!

```javascript
function count() {
    var cnt = 0
    return function() {
        cnt += 1
        return cnt
    }
}

var a = count()
console.log(a())
console.log(a())
var b = count()
console.log(b())
console.log(b())
console.log(a())

// 출력: 1 2 1 2 3
```

---

# 총정리 Review

2020.03.18

### HTML

- 브라우저 전쟁: 브라우저 파편화 --> 통합, 표준

- HTML 기본 개념(정의, 기본 구조 등)
- 태그
  - 그룹 컨텐츠, 텍스트 관련 요소, table, form, input
- **시맨틱 태그** 
  - 태그들의 의미담고 있음, 효과적인 마크업
  - nav, section, article, ...

> 태그가 어떠한 의미와 목적을 가지는 지 정리해두면 좋을 것 같다.

### CSS

- CSS 기본 개념 (정의, 활용법 등)

- **선택자 관련 개념들(우선순위) ★**

- 단위

  > px, rem, em, 등다양한 단위들 정리해두면 좋겠다.

- Box model

- Block, inline 요소 및 display

- position, float

  > 기본적으로 좌측 상단으로 정리
  >
  > absolute는 자기 자신의 위치를 버리기에 조심하기
  >
  > 브라우저 기준으로 고정하려면 fixed 사용하기
  >
  > 신문에서 많이 보이는 형태는 float!

> HTML 문서에서 무엇을 (선택자를 통해) style을 지정할 것인데 그때 요소들은 다 box model로 네모네모 형태이고 이 박스들이 어떻게 보일지 (display) 정의를 해주고 어디에 위치(position)할지 결정한다.  ~ 흐름기억하기

### JS

- JS 기초 개념

  - 데이터 타입(원시타입, 객체 타입), 연산자

    - 원시타입 :  숫자, 문자열 뿐 아니라 null, undefined 포함!!
    - 연산자 활용시 주의사항!

  - 객체 선언 및 활용

  - 배열, 순회

    > for - in 주의해야했던 점과 각각의 순회방식 정리해서 기억하기

  - 함수(함수 정의(화살표 함수까지) ~ 클로저)

    > 함수 정의 방법까지 기억! 문법 눈에 익햐두기

  - 이벤트, DOM 조작

    > 이벤트 : 클릭, copy, paste 와 같은 일들이 브라우저에서 발생하는 일들이 이벤트를 통해 정의되고 실행되고 있었다.

    >  DOM 조작에서 querySelector, querySelectorAll 두 메소드만 기억해주면 좋다





