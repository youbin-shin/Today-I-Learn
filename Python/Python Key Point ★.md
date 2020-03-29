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

### 클래스(Class) 

   - 객체를 표현하는 문법
- 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것
    - 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)

### 클래스의 정의

- 선언과 동시에 클래스 객체가 생성된다.
- 선언된 공간은 지역 스코프(local scope)로 사용된다.
- 정의된 attribute 중 변수는 멤버 변수로 불린다.
- 정의된 함수(`def`)는 메소드로 불린다.

```python
# 활용법
class ClassName:
    attributes
    methods
    
# ex
class User:
    """
    This is User Class
    """
    name = 'UserClass'

print(type(User)) # <class 'type'>
print(User.__doc__) # This is User Class
```

### 인스턴스

- 인스턴스 객체는 `ClassName()`을 호출함으로써 생성된다.
- 인스턴스 객체와 클래스 객체는 서로 다른 이름 공간을 갖는다.
- **인스턴스(instance) --> 클래스(class) --> 전역(global)** 순으로 탐색한다.
  - 인스턴스 = 클래스()
- 클래스는 특정 개념을 표현하는 껍데기고 실제 사용하려면 인스턴스를 생성해야 한다.
- 인스턴스와 객체는 같은 것을 의미
  - 보통 객체만 지칭시 단순히 객체라고 부름
  - 클래스와 연관지어 말할 때는 인스턴스라고 부름
  - `isinstance(확인하고 싶은 객체, 확인할 클래스)` 로 확인 가능

```python
# User class 인스턴스 생성
user = User()
print(type(user)) # <class '__main__.User'>
print(user.__doc__) # This is User Class

# user 인스턴스에게 이름 부여
user.name = 'youbin'

# User class 와 인스턴스 서로 다른 namespace 갖는다.
print(user.name) # youbin
print(User.name) # UserClass
```

```python
# 출력 차이 str vs repr

class User:
    username = ''
    password = ''
            
    
    def __str__(self): # for 사용자
        return 'print 안에 넣으면 이렇게 나오고'
    
    
    def __repr__(self): # for 개발자
        return '그냥 객체만 놔두면 이게 나오지요'
```

### 클래스의 생성과 소멸

- `__init__()`
  - 초기화
  - 인스턴스 객체가 만들어진 후에 호출되는 함수
  - 인스턴스에서 사용할 초기값들을 초기화함으로써 쵝화된 새 인스턴스를 얻을 수 있음
- `__del__()`
  - 소멸자, 파괴자
  - 인스턴스 객체가 소멸직전에 호출되는 함수

```python
def __init__(self):
    print('인스턴스가 생성된 후 자동으로 호출되는 메서드')
    
def __del__(self):
    print('인스턴스가 소멸되기 직전에 자동으로 호출되는 메서드')
```

## 8. oop advanced

### 클래스 변수, 인스턴스 변수

- 클래스 변수
  - 클래스의 속성
  - 모든 인스턴스가 공유
  - 클래스 선언 블록 최상단에 위치
  - `Class.class_variable` 과 같이 접근(할당)
- 인스턴스 변수
  - 인스턴스의 속성
  - 각 인스턴스들의 고유한 변수
  - `self.instance_variable` 로 접근(할당)
  - 인스턴스가 생성된 이후 `instance.instance_variable`로 접근(할당)

### 스태틱 메서드, 클래스 메서드, 인스턴스 메서드

인스턴스 3가지 메서드 접근 가능 --> 클래스 메서드, 스태틱 메서드 호출하지 X, 클래스 간 상속 있을 경우 다르게 동작

클래스 3가지 메서드 접근 가능 --> 인스턴스 메서드 호출 X

- 인스턴스 메소드
  - 인스턴스가 사용할 메서드
  - 메서드 정의 위에 어떠한 데코 X, 자동으로 인스턴스 메서드가 됨.
  - 첫번째 인자로 `self` 받도록 정의함! 이때 자동으로 인스턴스 객체가 `self`가 된다.
- 클래스 메서드
  - 클래스가 사용할 메서드
  - 정의 위에 `@classmethod` 데코 사용
  - 첫번째 인자로 `cls` 받도록 정의함! 이때 자동으로 클래스 객체가 `cls`가 된다.
- 스태틱 메서드
  - 클래스가 사용할 메서드
  - 정의 위 `@staticmethod` 데코 사용
  - 첫번째 인자 받지 X, 인자 정의 자유로게
  - 어떠한 인자도 자동으로 넘어가지 X

### 상속 ★

클래스의 가장 큰 특징 "상속"

부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성 높아짐.

- `issubclass(자식클래스, 부모클래스)` 클래스 상속 검사

- `super()` : 자식 클래스에 메서드 추가 구현 가능, 부모 클래스의 내용을 사용하고자 할 때 사용

  ```python
  class Person:
      def __init__(self, name, age, number, email):
          self.name = name
          self.age = age
          self.number = number
          self.email = email
      
      def greeting(self):
          print(f'반갑습니다. {self.name} 입니다.')
          
          
  class Student(Person):
      def __init__(self, name, age, number, email, student_id):
          super().__init__(name, age, number, email)
          self.student_id = student_id
          
      
  p1 = Person('유빈', '24', '5575','you@com')
  s1 = Student('기특', '8', '1294', 'love@com', '0129')        
  ```

## 3. function

### 함수 인자의 종류

- 위치 인자
- 기본 인자 (기본 인자 이후에 기본값이 없는 인자 사용 불가능)
- 키워드 인자
  - 키워드 인자 활용한 뒤 위치 인자 활용 X
  - `sep`, `end` 
- 가변 인자
  - tuple 형태로 처리
  - 매개변수에 `*`로 표현

### 함수의 리턴

어떠한 종류의 객체든 상관 X

오직 한 개의 객체만 반환

함수가 return되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

### 스코프

이름공간(namespace)는 `LEGB Rule` 가진다.

- Local scope : 정의된 함수
- Enclosed scope : 상위 함수
- Global scope : 함수 밖의 변수 혹은 import 된 모듈
- Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

## 4. data structure

### map, zip, filter

### comprehension

### 리스트 메소드

### 딕셔너리 메소드

### copy

## 6. errors

### 문법 에러와 예외의 이름

- 문법 에러 : SyntaxError

- 예외의 이름
  - ZeroDivisionError
  - NameError
  - TypeError
  - ValueError
  - IndexError
  - KeyError
  - ImprotError
  - KeyboardInterrupt

### 복수의 예외처리

하나 이상의 예외 모두 처리 가능

```python
try:
    codeblock1
except (예외1, 예외2):
    codeblock2
except 예외3 as err:
    codeblock3 # 에러구문 첨부 가능
except:
    codeblock4
    pass # 오류 회피
else: # try절이 예외를 일으키지 않을 때 실행
    codeblock5
finally: # 반드시 수행해야하는 문장 try문 떠날 때 항상 실행
    codeblock6 
```

- `raise` 로 예외 강제로 발생 가능

## 5. module

### 모듈 가져오기



## 2. control of flow

### 기본적인 반복문과 조건문

