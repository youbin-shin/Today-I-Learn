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

  


### DFS (깊이 우선 탐색)

비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.

[ 두가지 방법 ] 

모든 경우를 탐색하는 방법

1. 깊이 우선 탐색 (DFS, Depth First Search)
2. 너비 우선 탐색 (BFS, Breath First Search)



#### 그래프 표현

1. 인접 행렬

   M X M 크기의 2차원 배열을 이용하여 간선 정보를 저장

   배열의 배열(포인터 배열)

2. 인접 리스트

   각 정점마다 해당 정점으로 나가는 간선의 정보를 저장

   인접 행렬의 메모리 낭비를 줄여준다.

3. 간선의 배열

   간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장



#### DFS 알고리즘

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





























