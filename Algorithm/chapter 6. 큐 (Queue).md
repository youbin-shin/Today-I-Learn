# chapter6. 큐 (Queue)

> 2020.04.02

### 큐

#### 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료 구조
- 큐의 뒤(꼬리, Rear)에서는 삽입만! 큐의 앞(머리, Front)에서는 삭제(사용)만! 이루어지는 구조
- 선입선출 구조 FIFO(First In First Out)

#### 큐의 기본 연산

용어는 통상적일 뿐이지만 용어 사용을 추천!

- 삽입 : enQueue 
- 삭제 : deQueue

#### 큐의 주요 연산

| 연산          | 기능                                               |
| ------------- | -------------------------------------------------- |
| enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산        |
| deQueue()     | 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산 |
| createQueue() | 공백 상태의 큐를 생성하는 연산                     |
| isEmpty()     | 큐가 공백상태인지를 확인하는 연산                  |
| isFull()      | 큐가 포화상태인지를 확인하는 연산                  |
| Qpeek()       | 큐의 앞쪽(front)에서 원소를 삭제없이 반환하는 연산 |

#### 큐의 연산 과정

- front : 꺼내진 위치
- rear : 저장한 위치

1. 공백 큐 생성 : createQueue();

   front = rear = -1

2. 원소 A 삽입 : enQueue(A);

   front = -1

   rear += 1; Q[rear] = A

3. 원소 B 삽입 : enQueue(B)

   front = -1

   rear += 1; Q[rear] = B

4. 원소 반환/삭제 : deQueue();

   front += 1; A 꺼낸다.

5. 원소 C 삽입 : enQueue(C);

   front  = 0

   rear += 1; Q[rear] = C

6. 원소 반환/삭제 : deQueue();

   front += 1; B 꺼낸다.

7. 원소 반환/삭제 : deQueue();

   front += 1; C 꺼낸다.

   ※ front == rear : Q에 있는 모든 데이터가 꺼내진 상태

#### 큐의 구현

##### 선형큐

- 1차원 배열을 이용한 큐

  - 큐의 크기 = 배열의 크기
  - front : 저장된 첫번째 원소의 인덱스 --> 마지막으로 꺼낸 위치
  - rear : 저장된 마지막 원소의 인덱스 --> 마지막으로 저장된 위치

- 상태 표현

  - 초기 상태 : front = rear = -1

  - 공백 상태 : front = rear

  - 포화 상태 : rear = n - 1 (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)

    포화 상태에서 삽입하려는 것 X (overflow)

##### 초기 공백 큐 생성

- 크기 n인 1차원 배열 생성
- front = rear = -1로 초기화

##### 삽입 : enQueue(item)

```python
# 슈도코드
def enQueue(item):
    global rear
    if isFull(): ~
    else:
        rear += 1
        Q[rear] = item
```

##### 삭제 : deQueue()

```python
# 슈도코드
def deQueue():
    if (isEmpty() then Queue_Empty())
    else:
        front += 1
        return Q[front]
```

![image-20200402162414095](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200402162414095.png)

##### 공백상태 및 포화상태 검사 : isEmpty(), isFull()

```python
# 슈도코드
def isEmpty():
    return front == rear # 출력: True/False

def Full():
    return rear == len(Q) - 1
```

##### 검색 : Qpeek()

```python
# 슈도코드
def Qpeek():
    if isEmpty(): ...
    else:
        return Q[front + 1]
```

#### 선형 큐 이용시의 문제점

- 잘못된 포화상태 인식 : front 앞부분이 비어있는 데 rear에서 포화상태로 인식한 경우

- ~~해결방법 1: 매 연산이 이루어질 때마다 배열 앞으로 옮기기 (효율성 떨어짐)~~

- 해결방법 2

  - 1차원 배열을 사용!

    이때 배열의 **처음과 끝이 연결**되어 원형 형태의 큐를 이룬다고 가정하고 사용한다.

    원형 큐의 논리적 구조 (메모리 낭비 줄일 수 있음)

  - 원형 큐가 꽉 찬 경우 문제 발생!

### 연습문제 1 큐 기본 문제

세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고 큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.

```python
# solution 1
def enq(n):
    global rear
    if rear == len(q) - 1:
        print('Full')
    else:
        rear += 1
        q[rear] = n
    
q = [0] * 3
front = -1
rear = -1

rear += 1 # enq(1)
q[rear] = 1

rear += 1 # enq(2)
q[rear] = 2

rear += 1 # enq(3)
q[rear] = 3

while front != rear:
    front += 1 # print(dequeue())
    print(q[front])
```

```python
# solution 2
Q = []
Q.append(1) # enqueue(1)
print(Q.pop()) # dequeue()
```

### 원형 큐의 구조

#### 초기 공백 상태 

front = rear = 0

#### Index의 순환

front, rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후 처음 인덱스 0으로 이동시킨다.

이를 위해 나머지 연산자 mod 사용!

#### front 변수

공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠.

#### 삽입 위치 및 삭제 위치

|         | 삽입 위치               | 삭제 위치                 | 초기화            |
| ------- | ----------------------- | ------------------------- | ----------------- |
| 선형 큐 | rear  += 1              | front += 1                | front = rear = -1 |
| 원형 큐 | rear = (rear + 1) mod n | front = (front + 1) mod n | front = rear = 0  |

#### 원형 큐의 구현

##### 공백상태 및 포화상태 검사 : isEmpty(), isFull()

- 공백 상태 : front = rear

- 포화 상태 : 삽입할 rear의 다음 위치 = 현재 front

  (rear + 1) mod n = front

```python
# 슈도 코드
def isEmpty():
    return front == rear

def ifFull():
    return (rear + 1) % len(cQ) == front
```

##### 삽입 : enQueue(item)

```python
# 슈도 코드
def enQueue(item):
    global rear
    if isFull(): ...
    else:
        rear = (rear + 1) % len(cQ) # 꽉차있을 경우 대비하여 나눠줌.
        cQ[rear] = item
```

##### 삭제 : deQueue(), delete()

```python
# 슈도 코드
def delete():
    global front
    if isEmpty(): ...
    else:
        front = (front + 1) % len(cQ)
```

#### 연결 큐의 구조 (참고)

> 시간이 더 걸릴 수도 있기에 꼭 좋은 것만은 아니다!.

- 단순 연결 리스트 (Linked List)를 이용한 큐
  - Linked List : 저장위치가 따로 저장된 리스트
  - 큐의 원소 : 단순 연결 리스트의 노드
  - 큐의 원소 순서 : 노드의 연결 순서, 링크로 연결되어 있음.
  - front : 첫번째 노드를 가리키는 링크
  - rear : 마지막 노드를 가리키는 링크
- 상태 표현
  - 초기 상태 : front = rear = null
  - 공백 상태 : front = rear = null

#### 연결 큐의 구현

##### 초기 공백 큐 생성 : createLinkedQueue();

front = rear = NULL

- None : python
- NULL,/0, NIL, "" : 다른언어에서

(대문자NULL: 주소가 없다!! 정해지지 않았다.)

##### 공백 상태 검사 : isEmpty()

```python
# 슈도 코드
def isEmpty():
    return front == None
```

##### 삽입 : enQueue(item)

```python
# 슈도 코드
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

def enQueue(item):
    global front, rear
    newNode = Node(item) # 새로운 노드 생성
    if isEmpty(): # 큐가 비어있다면
        front = newNode
    else:
        rear.next = newNode
    rear = newNode
```

### 우선순위 큐 (Priority Queue)

- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
- 우선순위 큐의 적용 분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영 체제의 테스크 스케줄링

#### 우선순위 큐의 구현

- 배열(python list)을 이용한 우선순위 큐
- 리스트(python linked list)를 이용한 우선순위 큐

#### 배열을 이용한 우선순위 큐

- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨.
- 문제점
  - 배열을 사용하므로 삽입/삭제 연산시 원소의 재배치 발생함.
  - 소요 시간, 메모리 낭비가 큼.

### 큐의 활용 : 버퍼 (Buffer)

- 버퍼
  - 데이터를 한곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
- 버퍼의 자료 구조
  - 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.
  - 순서대로 입력/출력/전달되어야 하므로 FIFO방식의 자료 구조인 큐가 활용된다.

### 연습문제 2 마이쮸 시뮬레이션 문제

Queue 를 이용하여 마이쮸 나눠주기 시뮬레이션을 해보자

1번이 줄을 선다. 1번이 한개의 마이쮸를 받는다.

1번이 다시 줄을 선다. 새로 2번이 들어와 줄을 선다.

1번이 두 개의 마이쮸를 받는다. 1번이 다시 줄을 선다. 새로 3번이 들어와 줄을 선다.

2번이 한 개의 마이쮸를 받는다. 2번이 다시 줄을 선다. 새로 4번이 들어와 줄을 선다.

1번이 세 개의 마이쮸를 받는다. 1번이 다시 줄을 선다. 새로 5번이 들어와 줄을 선다.

3번이 한 개의 마이쮸를 받는다. ... 반복한다고 한다.

20개의 마이쮸가 있을 때 누가 가져갈까?

```python
# solution
N = 20 # 마이쮸 개수
q = [(1, 0)] # 1번이 줄을 서고 아직 받지 않은 상태
j = 1 # 새롭게 줄을 서는 사람 번호
last = 0 # 마지막으로 받아간 사람
print(N,q)
while N>0: # 마이쮸가 남아있는 동안
    i,m = q.pop(0) # 줄의 맨 앞사람, i번, m이전에 받은 개수
    m += 1 # 이번에 받을 개수
    N -= m # 남은 마이쮸개수
    j += 1 # 새로 줄서는 사람의 번호
    q.append((i,m)) # 맨 앞사람이 m개를 받아서 줄을 섬
    q.append((j,0)) # 새로 줄서는 사람. 아직 마이쮸를 받지 않음
    last = i
    print(i,m,N,q)
print(last)
```

### BFS

### 최단경로

### 실습 1, 2