# Python Key Point ★

## 1. python intro ★

### 시퀀스 자료형의 특징과 활용방법

#### 시퀀스

- 시퀀스 : 데이터가 순서대로 나열된 형식
- 시퀀스 타입
  - list
  - tuple 
    - immutable (수정 불가능, 읽기만 가능)
  - range
  - string
  - binary
- **시퀀스에서 활용가능한 연산자/함수**
  - x `in` s , x `not in` s
  - s1 `+` s2 : concatenation
  - s `*` n : n 번만큼 반복하여 더하기
  - `s[i]` : indexing
  - `s[i:j]` : slicing
  - `s[i:j:k]` : k간격으로 slicing
  - len(s) : 길이
  - min(s), max(s)
  - s.count(x) : x의 개수

### set

순서 X 자료구조

- 집합
- `{}` 로 생성, 중복값 X
- 빈 집합 만들 시, `set()` 사용 ※ `{}` 사용 불가능

#### 활용법

- a` -` b , `a.difference(b)`
- a `|` b , `a.union(b)`
- a `&` b , `a.intersection(b)`

### dictionary

`key` 와 `value` 쌍으로 이뤄져 있다.

- 아이템이 삽입되는 순서 갖고 O
- `{}` 를 통해 만들며, `dict()`로 만들 수 있다.
- key : immutable 모든 것 가능
  - immutable 값 : string, integer, float, boolean, tuple, range
- value : list, dictionary 포함한 모든 것 가능

### 데이터 타입

#### sequence (Ordered)

- 'sting' - immutable
- [list] - mutable
- (tuple) - immutable
- range() - immutable

#### Unordered

- {set} - mutable
- {dictionary: } - mutable

## 7. oop basic ★

### 클래스의 정의

### 클래스와 인스턴스

### 생성자

## 8. oop advanced

### 클래스 변수, 인스턴스 변수

### 스태틱 메소드, 클래스 메소드, 인스턴스 메소드

### 상속

## 3. function

### 함수 인자의 종류

### 함수의 리턴

### 스코프

## 4. data structure

### map, zip, filter

### comprehension

### 리스트 메소드

### 딕셔너리 메소드

### copy

## 6. errors

### 문법 에러와 예외의 이름

### 복수의 예외처리

### 

## 5. module

### 모듈 가져오기

### 

## 2. control of flow

### 기본적인 반복문과 조건문

### 

### 

### 

### 