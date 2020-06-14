# chapter 4. 스택 1 ★

> 2020.02.13 알고리즘_5

- 객체지향 언어 vs 절차지향 언어

  차이는 데이터의 연관의 유무

  객체 지향 언어는 받은 데이터에 대해 클래스로 묶어 준다.

  반면 절차 지향 언어는 데이터를 받는 것에서 끝. 그이상 연결고리는 없다.

---

### 스택

- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(LIFO, Last-In-First_Out)

- 구현하기 위해 필요한 자료구조와 연산

  - 자료구조 : 자료를 선형으로 저장할 저장소

    C언어에서 배열 사용 가능 (Python : list)

    저장소 자체를 스택이라고 부르기도 함

    스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.

  - 연산

    삽입 : 저장소에 자료 저장 / 보통 push라 부름

    삭제 : 저장소 자료 꺼냄 / 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄 / 보통 pop이라 부름

    스택이 공백인지 아닌지 확인하는 연산 : isEmpty / 공백은 top  -1확인

    스택의 top 에 있는 item(원소)를 반환하는 연산 :peek


#### 스택의 알고리즘

```python
# push
s.append(item)

# pop
def pop():
    if len(s) == 0:
        # underflow : 없는 데 찾으려고 하는 것
        return
    else:
        return s.pop(-1)
    
# peek
def pop():
    if len(s) == 0:
        # underflow
        return
    else:
        return s[-1]
```

#### 연습문제 1 _  스택 구현하기

구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서  출력하기

```python
stack = [0] * 10
top = -1

# push 연산
for i in range(3):
    stack[top + 1] = i
    top += 1
    
# pop 연산
# t 라는 임시변수에 저장 후 출력
for i in range(3):
    t = stack[top]
    top -= 1
    print(t)
```

#### 스택의 응용 1 - 괄호 검사

```python
stack = [0] * 100
top = -1
str = "(()()))"

wrong = 0
for i in range(len(str)):
    if str[i] == '(':
        top += 1
        stack[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            wrong = 1
            break
        if stack[top] == '(':
            top -= 1
if top == -1 and not wrong:
    print("correct!")
else:
    print("wrong")
```

```python
# My code

stack = [0] * 10
emptylst = [0] * 10
top = -1

check = list(map(str,input()))

for i in range(len(check)):
    stack[top + 1] = check[i]
    top += 1
    if check[i] == ')'and stack[top - 1] == '(':
        stack[top - 1] = 0
        stack[top] = 0
        top -= 2

if stack == emptylst:
    print('okay')
else:
    print('error')
```

#### 스택의 응용2 - function call

프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

후입선출 구조로 스택을 이용하여 수행 순서를 관리

### 재귀호출

자기자신을 호출하여 순환 수행

problem ) 경우에 따라 중복 호출 발생

- sol 1 : Memoization

  실행할 때 이전에 계산한 값을 메모!!하여 실행속도를 빠르게 하는 기술

  ```python
  # 피보나치 수 memoizaiton 알고리즘
  
  def fibo1(n):
      global memo
      if n >= 2 and len(memo) <= n:
          memo.append(fibo1(n-1) + fibo1(n-2)) # 메모
      return memo[n]
  
  memo = [0, 1]
  ```

- sol 2 : DP (Dynamic Programming)

  동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘

  작은 부분 문제들을 해결한 뒤에 큰 부분의 문제를 해결하는 알고리즘

  ```python
  # 피보나치 수 DP 적용 알고리즘
  
  def fibo2(n):
      f = [0, 1]
      
      for i in range(2, n+1):
          f.append(f[i-1] + f[i-2])
          
      return f[n]
  ```

- DP 의 구현 방식

  - recursive 방식 : fib1()
  - iterative 방식 : fib2()

  ```python
  # 피보나치 수열
  # 재귀함수, memoization, dp 방식 3가지를 이용하여 각각 호출을 count 해보자.
  
  def fibo(n):
      print("fibo(",n,") is called")
      if n < 2:
          return n
      else:
          return fibo(n-1) + fibo(n-2)
  
  
  memo = [0, 1]
  
  def fibo1(n):
      global memo
      print("fibo1(",n,") is called")
      if n >= 2 and len(memo) <= n:
          memo.append(fibo1(n-1) + fibo1(n-1))
      return memo[n]
  
  def fibo2(n):
      f = [0, 1]
  
      print("fibo2(",n,") is called")
      for i in range(2, n+1):
          f.append((f[i-1] + f[i-2]))
  
      return f[n]
  
  print("recursive fibo")
  fibo(5)
  
  print("recursive + memoization fibo")
  fibo1(5)
  
  print("dynamic fibo")
  fibo2(5)
  ```

  ```python
  # 출력
  recursive fibo
  fibo( 5 ) is called
  fibo( 4 ) is called
  fibo( 3 ) is called
  fibo( 2 ) is called
  fibo( 1 ) is called
  fibo( 0 ) is called
  fibo( 1 ) is called
  fibo( 2 ) is called
  fibo( 1 ) is called
  fibo( 0 ) is called
  fibo( 3 ) is called
  fibo( 2 ) is called
  fibo( 1 ) is called
  fibo( 0 ) is called
  fibo( 1 ) is called
  recursive + memoization fibo
  fibo1( 5 ) is called
  fibo1( 4 ) is called
  fibo1( 3 ) is called
  fibo1( 2 ) is called
  fibo1( 1 ) is called
  fibo1( 1 ) is called
  fibo1( 2 ) is called
  fibo1( 3 ) is called
  fibo1( 4 ) is called
  dynamic fibo
  fibo2( 5 ) is called
  ```

#### 재귀함수

```python
def func(n 매개 변수) --> 매개 변수 : **문제의 크기**이자 식별
	if 기저사례
	else: func
	return 해
```

일반적으로 재귀로 풀경우 언제 끝낼지에는 매개변수 기준으로 판단된다.

그외의 외부의 값으로 판단할수있다면 재귀로 풀필요없다!

문제의 크기를 줄여가면서 푸는 방식

```python
# 재귀 함수는 기본적으로 반복적 작업
# for, while 을 없이 가능

# for 이용시에
for i in range(3):
    print('Hello')
# 재귀로 위의 코드를 작성할 시에
def printHello(i):
    if i == 3:
        return
    else:
        print('Hello')
        printHello(i+1)
printHello(0)
# 재귀 sol2
def printHello(i):
    if i < 3:
        print('Hello')
        printHello(i+1)
printHello(0)

# 재귀 원하는 횟수만큼
def printHello(i, n):
    if i == n:
        return
    else:
        print('Hello')
        printHello(i+1, n)
printHello(0, 3)


# 재귀 제대로 이해하기
def printHello(i, n):
    if i == n:
        return
    else:
        print(i, 'Hello') # 순서대로 진행
        printHello(i+1, n)
        print(i, 'Hello') # 역순으로 진행
printHello(0, 3)

# 출력 0 Hello/ 1 Hello/ 2 Hello/ 2 Hello/ 1 Hello/ 0 Hello

# 재귀 제대로 이해하기2
cnt = 0
def printHello(i, n):
    if i == n:
        global cnt
        cnt += 1
        return
    else:
        printHello(i+1, n)
        printHello(i+1, n)
printHello(0, 3)
print('cnt=', cnt)
# 출력 2^3 = 8(2진 트리) 이기에 cnt=8 로 출력된다.


# 재귀 제대로 이해하기3
cnt = 0
def printHello(i, n): # i: 함수 호출 깊이, n: 단말노드, 마지막 단계 판단하기 위한 값
    if i == n:
        global cnt
        cnt += 1
        return
    else:
        printHello(i+1, n)
        printHello(i+1, n)
        printHello(i+1, n)
printHello(0, 3)
# 출력 3^3
```

```python
# 피보나치 일반적인 재귀 함수 코드
# 중복 호출이 많아 오래걸림
def fibo(n):
    if n <=2: return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(35))

# memoization 이용하여 작성한 재귀 함수 코드
memo = [0, 1, 1] + [0] * 100
def fibo_memo(n):
    if n <=2: return 1
    if memo[n]:return memo[n]
    memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]
print(fibo_memo(35))

# DP 이용
# memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현한 것이 성능에 효율적
def fibo_iter(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(2, n + 1): # i는 문제를 식별하는 값
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
```




## DFS (깊이 우선 탐색)

비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.

[ 두가지 방법 ] 

모든 경우를 탐색하는 방법

1. 깊이 우선 탐색 (DFS, Depth First Search)
2. 너비 우선 탐색 (BFS, Breath First Search)

### 그래프

- 그래프는 아이템들과 이들 사이의 연결 관계

- 그래프는 정점 vertex들의 집합과 간선edge들의 집합으로 구서오딘다.

  - M:정점의 개수
  - 최대 간선의 개수 : M(M-1)/2

  선형(1:1) 자료구조나 트리(1:N) 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이하다.

그래프 유형

(그래프가 다 연결되어 있는 그래프를 `결합 컴포넌트(connected component)`라고 부른다.)

모든 정점

- 무향그래프 Undirected Graph

- 유향 그래프 Directed Graph 

  선행, 대소 관계

  2 3 4

- 가중치 그래프 Weighted Graph

- 사이클 없는 방향 그래프 DAG, Directed Acyclic Graph

  4 5

  5는 tree는 결합 컴포넌트가 되기 위한 최소의 간선을 가짐

- 그림

  1 2 3

  4 5

![그래프 종류](https://user-images.githubusercontent.com/60081201/76926968-1bd4f580-6921-11ea-85df-233d07836cb8.JPG)

#### 그래프 경로

- 경로란 간선들을 순서대로 나열한 것

  - 간선들 (0,2), (2, 4), (4, 6)
  - 정점들: 0-2-4-6

- 경로 중 한 정점을 최대 한번만 지나가는 경로 : 단순 경로

  0 - 2 -4 - 6, 0 - 1 - 6

- 시작한 정점에서 끝나는 경로: 사이클 Cycle

  1 - 3 - 5 - 1

#### 그래프 표현 (저장)

간선의 정보를 저장하는 방식, 메모리나 성능을 고려하여 결정

1. **인접 행렬 (Adjacent matrix)**

   M * M 크기의 2차원 배열을 이용해서 간선 정보를 저장

   배열의 배열(포인터 배열)

   - 행의 정보 : 진출차수
   - 열의 정보 : 진입차수

   단점 : 메모리 차지, 실행 시간 많이 걸림

2. **인접 리스트 (Adjacent List)**

   python List를 이용하여 구현하기 좋음 추천추천

   각 정점마다 해당 정점으로 나가는 간선의 정보를 저장

   인접 행렬의 메모리 낭비를 줄여줌

3. **간선의 배열**

   간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장



### DFS 알고리즘

1.  시작 정점 v를 결정하여 방문의 표시를 해둔다.
2. 정점 v에 인접한 정점 중
   1. 방문하지 않은 정점 w가 있으면,  정점 v를 스택에 push 하고 정점 w를 방문한다. w를 v로 하여 2. 반복한다.
   2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.반복한다.
3. 스택이 공백이 될 때까지 2.를 반복한다.

```python
# 재귀 호출로 스택 처리

visited 
DFS(v)
	v 방문
    visited[v] <- true
    while(v의 인접 정점)
    	w <- 인접 정점
        if w 가 방문하지 않은 정점이면
        	DFS(w)
            
end DFS() 
```

```python
visited[], stack[] 초기화
visited = [0] * len(V)
stack = []
graph = [[0]*len(V) for _ in range(len(V))]

DSF(v)
	stack.append(v) # push(v)
    while (len(stack)): # stack is not empty
        v = stack.pop(-1)
        if visited(v) != 1: # v가 방문하지 않은 정점이라면
            visited[v] = 1 # true
            v 방문 # 출력, 계산
            
            for w in (len(V)): 
                if graph[v][w] == 1 and visied[w] == 0: # v의 인접 정점 찾기
                    stack.append(w)
                if w가 방문하지 않은 정점이라면:
                    push(w)

end DFS()                    
```



```python
import sys

sys.stdin = open("input.txt","r")

# 인덱스 0부터이기에 입력에 -1로 계산하여 푼 코드 
# 인접 행렬

vertex, line = map(int, input().split())

graph = [[0] * (vertex) for _ in range(vertex)]
visited = [0] * (vertex)
stack = []

for i in range(line):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

v = 0
stack.append(v)
while (len(stack) > 0):
    v = stack.pop(-1)

    if visited[v] != 1:
        visited[v] = 1
        print(v+1, end=' ')

        for w in range(len(graph[v])):
            if graph[v][w] == 1 and visited[w] == 0:
                stack.append(w)

print()
for i in range(vertex):
    print(graph[i])


```

```python
#input.txt
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
```

```python
# 출력
1 3 7 6 5 2 4 
[0, 1, 1, 0, 0, 0, 0]
[1, 0, 0, 1, 1, 0, 0]
[1, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 0, 0, 1, 0]
[0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 1, 1, 0, 1]
[0, 0, 1, 0, 0, 1, 0]
```

```python
# sol 2 0을 추가하여 인덱스 그대로 받는 코드
# 입력, 출력 위와 동일

vertex, line = map(int, input().split())

graph = [[0] * (vertex+1) for _ in range(vertex+1)]
visited = [0] * (vertex+1)
stack = []

for _ in range(line):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

v = 1
stack.append(v)
while (len(stack) > 0):
    v = stack.pop(-1)

    if visited[v] != 1:
        visited[v] = 1
        print(v, end=' ')

        for w in range(1, len(graph[v])):
            if graph[v][w] == 1 and visited[w] == 0:
                stack.append(w)

print()
for i in range(vertex):
    print(graph[i])
```

```python
# 재귀함수를 이용한 recursive DFS

def DFSr(v):
    print(v, end=' ')
    visited[v] = True

    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            DFSr(i)
    return


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * 8
G = [[0] * 8 for _ in range(8)]
stack = [0] * 10
top = -1

for i in range(0, len(edges), 2):
    G[edges[i]][edges[i + 1]] = 1
    G[edges[i + 1]][edges[i]] = 1

DFSr(1) # 출력 1 2 4 6 5 7 3
```





























