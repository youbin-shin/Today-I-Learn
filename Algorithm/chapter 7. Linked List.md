# chapter 7. Linked List

> A형 시험에서는 실제로 구현해서 사용하기 드물지만 
>
> B형에서 중요한 구조!!!

### List

- 순서를 가진 데이터의 집합을 가리키는 추상 자료형(abstract data type)
- 동일한 데이터를 갖고 있어도 상관 X
- 구현 방법
  1. 순차 리스트 : 배열을 기반으로 구현된 리스트 (연속된 메모리 공간)
  2. 연결 리스트 : 메모리의 동적 할당을 기반으로 구현된 리스트

#### 리스트의 주요 함수

- `addtoFirst()` : 리스트의 앞쪽에 원소 추가하는 연산
- `addtoLast()` : 리스트의 뒤쪽에 원소 추가하는 연산
- `add()` : 리스트의 특정 위치에 원소를 추가하는 연산
- `delete()` : 리스트의 특정 위치에 있는 원소를 삭제하는 연산
- `get()` : 리스트의 특정 위치에 있는 원소르 리턴하는 연산

#### 순차 리스트

##### 구현방법

- 1차원 배열에 항목들을 순서대로 저장
- 데이터의 종류와 구조에 따라 구조화된 자료구조를 만들어 배열로 생성

##### 데이터 접근

배열의 인덱스를 이용하여 원하는 위치의 데이터에 접근 가능

##### 연산

1. 삽입 연산 : 삽입 위치 다음의 항목들을 오른쪽(뒤쪽)으로 이동해야 함. (`insert()` 내부 작업)
2. 삭제 연산 : 삭제 위치 다음의 항목들을 왼쪽(앞쪽)으로 이동해야 함. (`pop()` 내부 작업)

##### 문제점

- 자료의 삽입/삭제 연산 과정에서 연속적인 메모리 배열을 위해 원소들을 이동시키는 작업이 필요
- 원소의 개수가 많고 삽입/삭제 연산이 빈번하게 일어날수록 작업 소요시간 크게 증가
- 배열의 크기가 정해져 있는 경우, 실제로 사용될  메모리보다 크게 할당하여 메모리의 낭비를 초래할 수 있고 반대로 할당된 메모리보다 많은 자료를 사용하여 새롭게 배열을 만들어 작업하는 경우가 발생 가능

### 연결 리스트 (Linked List)

- 자료의 논리적인 순서와 메모리 상의 물리적인 순서 일치 X
- 개별적으로 위치하고 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룸
- 링크(다음 자료에 대한 정보)를 통해 원소에 접근! (순차리스트처럼 물리적인 순서를 맞추기 위한 작업 필요 X)
- 자료구조의 크기를 동적으로 조정 가능 --> 메모리의 효율적인 사용
- 단점 - 자료를 읽을 때 처음값부터 읽어나가야 함.

##### 기본 구조

- 노드 → `class`로 정의
  - 연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료단위
  - 구성 요소
    1. 데이터 필드 : 원소 값 저장하는 자료구조, 저장할 원소의 종류나 크기에 따라 구조를 정의하여 사용
    2. 링크 필드 : 다음 노드의 주소를 저장하는 자료구조
- 헤드 : 리스트의 처음 노드를 가리키는 레퍼런스

### 단순 연결 리스트 (Singly Linked List)

#### 연결 구조

- 노드가 하나의 링크 필드에 의해 다음 노드와 연결되는 구조를 가진다.
- 헤드가 가장 앞의 노드(`head`)를 가리키고 링크 필드가 연속적으로 다음 노드를 가리킨다.
- 최종적으로 **NULL을 가리키는 노드**가 리스트의 **마지막 노드**(`tail`)이다.

```python
# 단일(단순) 연결 리스트 이해하기
class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n
        print(d, '생성')
    def __del__(self):
        print(self.data, '삭제')
        
arr = []
for i in range(5):
    arr.append(Node(i))
# 출력: 0생성; 1생성; 2생성; 3생성; 4생성; 0삭제; 1삭제; 2삭제; 3삭제; 4삭제
```

```python
# 단일(단순) 연결 리스트 활용 예제
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.size = 0  # 노드의 수

    def inser_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조

def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return        
    cur = lst.head
    print(lst.size)
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next


mylist = LinkedList()
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
mylist.head = n1
mylist.size = 5
printList(mylist)


# 출력 
# 5
# 1 2 3 4 5 
```

#### 기본 코드 정리

##### class 정의

```python
# class 만들기
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.tail = None # 마지막 노드
        self.size = 0  # 노드의 수

    def inser_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조
```

##### printList 함수 (디버깅 가능)

```python
def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head
    print(lst.size, end=': ')
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next
    print()
```

##### insertLast 함수

```python
def insertLast(lst, new): # new : 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # else 문 뒤 코드 순서 바뀌면 안된다!!
        lst.tail.next = new
        lst.tail = new
    lst.size += 1
```

##### deleteLast 함수

```python
def deleteLast(lst):
    if lst.head is None: return
    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None: # list 한개일 경우 pre.next 에서 오류나기에 걸러주기
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
        lst.size -= 1
```

##### insertFirst 함수

```python
def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1
```

##### deleteFirst 함수

```python
def deleteFirst(lst):
    if lst.head is None: return
    # 노드가 1개 일 경우 주의하기
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1
```

##### insertAt 함수

```python
def insertAt(lst, idx, new): # idx : 인덱스 값
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막 추가하는 경우, idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    else:
        # 중간에 추가하는 경우 (head, tail 변화 X)
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1
```

##### deleteAt 함수

```python
def deleteAt(lst, idx):
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    elif idx >= lst.size:
        deleteLast(lst)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1
```

##### 참고 비교 코드

```python
# 단일(단순) 연결 리스트 + 삽입 (마지막 노드 모를 경우)
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.size = 0  # 노드의 수

    def inser_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조


def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head
    print(lst.size, end=': ')
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next
    print()

def inserLast(lst, new): # new : 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = new
    else:
        # 마지막 노드 찾기!
        cur = lst.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new
    lst.size += 1


mylist = LinkedList()
for i in range(5):
    inserLast(mylist, Node(i))
    printList(mylist)

# 출력
# 1: 0 
# 2: 0 1 
# 3: 0 1 2 
# 4: 0 1 2 3 
# 5: 0 1 2 3 4 

```

```python
# 단일(단순) 연결 리스트 + 삽입 (마지막 노드 알 경우)
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.tail = None # 마지막 노드
        self.size = 0  # 노드의 수

    def inser_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조


def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head
    print(lst.size, end=': ')
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next
    print()

def inserLast(lst, new): # new : 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # else 문 뒤 코드 순서 바뀌면 안된다!!
        lst.tail.next = new
        lst.tail = new
    lst.size += 1


mylist = LinkedList()
for i in range(5):
    inserLast(mylist, Node(i))
    printList(mylist)
```

### 이중 연결 리스트 (Doubly Linked List)

- 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
- 두 개의 링크 필드(prev, next)와 한개의 데이터 필드(data)로 구성

#### 삽입 연산

cur가 가리키는 노드 다음으로 D값을 가진 노드를 삽입하는 과정

1. 메모리를 할당하여 새로운 노드 new를 생성하고 데이터 필드에 'D'를 저장한다.

   ![linkedlist](https://user-images.githubusercontent.com/60081201/78963271-edb69000-7b31-11ea-8ca4-831419e77e32.JPG)

   - 새로 추가되는 연결 노드 설정한 뒤 기존에 있던 연결 노드 설정하는 것이 실수를 줄일 수 있다.

2. cur의 next를 new의 next에 저장하여 cur의 오른쪽 노드를 삽입할 노드 new의 오른쪽 노드로 연결한다.

3. new의 주소를 cur의 next에 저장하여 노드 new를 cur의 오른쪽 노드로 연결한다.

4. cur에 있는 링크 값을 new의 prev에 저장하여 cur를 new의 외왼쪽 노드로 연결한다.

5. new의 주소를 new의 오른쪽 노드의 next에 저장하여 노드 new의 오른쪽 노드의 왼쪽 노드로 new를 연결한다.

   ![linkedlist2 JPG](https://user-images.githubusercontent.com/60081201/78963264-eb543600-7b31-11ea-83c3-a080c200f001.png)

 #### 삭제 연산

- cur가 가리키는 노드를 삭제하는 과정

  삭제할 노드만 찾으면 된다.

  ![linkedlist3](https://user-images.githubusercontent.com/60081201/78963267-ed1df980-7b31-11ea-97f7-1fa188838a15.JPG)

  cur.prev.next = cur

  cur.next.prev = cur

- 빈리스트일 경우, 처음 삭제/ 주중간 삭제/ 마지막 삭제

#### 구현 코드 ★

```python
class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addLast(lst, new): # 하나하나 인자를 lst에 추가하는 함수
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.prev = lst.tail
        lst.tail.next = new
        lst.tail = new # 위 코드와 순서바뀌면 X
    lst.size += 1

def addList(lst, arr): # arr를 lst에 한번에 추가하는 함수
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break # 조건에 따라서 (변경가능)
            cur = cur.next
        if cur is None: # 마지막위치에 추가 (prev보다 먼저 해야함)
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None: # cur == lst.head 맨앞에 추가
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else: # 중간
            prev = cur.prev # prev 변수에 넣은 것 뿐!! 복잡해져서
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)


def printList(lst): # 출력 코드
    if lst.head is None: return
    else:
        cur = lst.head # 순서대로 출력하는 코드
        while cur is not None: 
            print(cur.data, end=' ')
            cur = cur.next
        print()
        cur = lst.tail # 거꾸로 출력하는 코드
        while cur is not None: 
            print(cur.data, end=' ')
            cur = cur.prev
        print()

mylist = LinkedList()

arr = [1, 3, 5, 7, 9]
# 1번
for val in arr:
    addLast(mylist, Node(val))
printList(mylist)

# 1번 코드와 동작 같다!
addList(mylist, arr)
printList(mylist)
```

#### Josephus Problem

23명의 병사가 원으로 둘러있을 때 12시방향위치한 병사부터 3명씩 건너뛰며 죽는다!

(1 -> 4 -> 7 -> 10 -> 13 -> 17 -> 20 -> 23 -> 5 ->...)

1. 배열 이용
   - 첫번째 병사의 값을 음수 처리 후 이동
   - 이동시 병사의 값을 확인하여 count
   - 음수로 변한 병사의 명수를 저장
   - 남은 병사의 명수가 2명이면 남은 병사의 번호 반환
   - 문제점
     1. 배열 내 순환 횟수 증가
     2. 불필요한 연산 발생
2. 연결 리스트 
   - 노드를 생성하여, 각 노드에는 병사의 위치를 데이터로 저장
   - 첫 번째 병사를 시작하고 3만큼 이동
   - 병사를 삭제하고 3만큼 이동한다.
   - 남은 병사 수가 2이면 각 병사의 데이터를 확인
   - 불필요한 순간 X

---

### 삽입 정렬 (Insertion Sort)

자료 배열의 모든 원소들을 앞에서부터 차례대로 이미 정렬된 부분과 비교하여 자신의 위치를 찾아냄으로써 정렬을 완성한다.

#### 정렬 과정

- 정렬할 자료를 두 그룹으로 나눈다.
  - 부분집합 S : 정렬된 앞부분의 원소들
  - 부분집합 U: 아직 정렬되지 않은 원소들
- 정렬되지 않은 부분집합 U의 원소를 하나식 꺼내서 이미 정렬되어 있는 부분집합 S의 마지막 원소부터 비교하여 위치를 찾아 삽입한다.
- 삽입 정렬을 반복하면서 부분집합 S의 원소는 하나씩 늘리고 부분집합 U의 원소는 하나씩 감소하게 되고 부분집합 U가 공집합이 되면 삽입정렬이 완성된다.

#### 시간 복잡도

최선의 경우 : O(n) / 최악의 경우 : O(n^2)

#### 코드 구현

배열에 비해 linked list 가 구현은 복잡하지만 효율은 높아진다.

```python
# 배열로 구현 할 경우
arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)

# i : 정렬된 집합과 정렬되지 않은 집합의 경계!!
for i in range(1, N): # i가 정렬되지않은 집합 시작
    # 값이 큰 정렬된 집합의 원소들은 지나가고 같거나 작으면 거기에 삽입
    tmp = arr[i]
    # print(arr[:i], arr[i:]) 정렬된 집합, 정렬되지 않은 집합
    j = i - 1
    while j >= 0 and arr[j] > tmp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = tmp

print(arr)
```

### 병합 정렬 (Merge Sort)

여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

#### 분할 정복 알고리즘 활용

자료를 최소 단위로 문제까지 나눈 후 차례로 정렬하여 최종 결과를 얻어냄 (top-down 방식)

분할 → 정복 →  병합(합병)

#### 시간 복잡도

O(nlogn)

#### 병합 정렬 과정

{68, 10, 30, 2, 16, 8, 31, 22} 병합 정렬하는 과정

1. 분할 단계 : 전체 자료 집합에 대하여 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.

![linkedlist 4JPG](https://user-images.githubusercontent.com/60081201/78963268-ed1df980-7b31-11ea-84c1-f8d1e94561c4.JPG)

2. 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합

```python
# 분할 과정 수도코드
def mergo_sort(m):
    if len(m) <= 1: # 사이즈가 0이거나 1인 경우, 바로 리턴
        return m
    # 1. divide
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    
    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 2. conquer : 분할된 리스트 병합
    return merget(left, right)
```

```python
# 병합 과정 수도코드
def merge(left, right):
    result = [] # 두개의 분할된 리스트를 병합하여 result 만듦
    
    while len(left) > 0 and len(right) > 0: # 양쪽 리스트에 원소 남아있는 경우
        # 두 서브 리스트의 첫 원소들을 비교하여 작은 것 부터 result에 추가
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    if len(left) > 0: # 왼쪽 리스트에 원소가 남아있는 경우
        result.extend(left)
    if len(right) > 0: # 오른쪽 리스트에 원소가 남아있는 경우
        result.extend(right)
    return result
```

### 리스트를 이용한 스택

### 우선순위 큐 (Priority Queue)

- 구현
  - 배열을 이용한 우선순위 큐
  - 리스트를 이용한 우선순위 큐
- 기본연산
  - 삽입 : enQueue
  - 삭제 : deQueue

#### 배열을 이용한 우선순위 큐

- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치!
- 문제점
  - 배열을 사용하여 삽입/삭제 연산시 원소의 재배치 발생
  - 소요시간이나 메모리 낭비 큼

#### 리스트를 이용한 우선순위 큐

- 연결 리스트를 이용하여 자료 저장
- 원소를 삽입하는 과정에서 리스트 내 노드의 우너소드로가 비교하여 적절한 위치에 노드를 삽입하는 구조 
- 리스트의 가장 앞쪽에 최고 우선순위가 위치

- 장점
  - 삽입/삭제 연산 이후 원소의 재배치 필요 X
  - 메모리의 효율적인 사용 가능

![image-20200410130448798](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200410130448798.png)