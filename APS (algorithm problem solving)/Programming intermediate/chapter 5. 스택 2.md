# chapter 5. 스택 2

> 2020.02.19 알고리즘_6



## 추가 개념

- **위상 정렬** : 문제 작업 순서 solution

  진입 간선이 없는 정점들을 선택해주고 해당하는 간선들( 진출 간선들 )을 제거해주면서 이 작업을 계속하는 방법 

  - 위상 정렬 - DFS 기반

    : DFS로 끝까지 경로를 간 뒤에 그 정점을 저장한 후 역순으로 출력하는 방법

    정점으로 방문하지 않은 곳은 방문하지만 방문한 곳이 없으면 return 되면서 저장

    

- deque : 양방향 list

  |          | List | Deque |
  | :------: | ---- | ----- |
  | indexing | O(1) | Q(n)  |
  | slicing  | O(1) | O(1)  |
  | pop(-1)  | O(1) | O(1)  |
  | popleft  | O(n) | O(1)  |
  |  insert  | O(n) | O(1)  |
  |  remove  | O(n) | O(1)  |

  



## 계산기

### 문자열 수식 계산 방법 

> 컴퓨터 내에 계산하는 방법

1. 중위 표기법을 후위 표기법으로 변경 (스택 이용)

- 중위표기법: 연산자를 피연산자 가운데 표기 ex) A + B

- 후위 표기법: 연산자를 피연산자 뒤에 표기 ex) AB+

  ex) `A*B-C/D ` -> `(AB*) - (CD/)` -> `AB*CD/-`

  [ 변환 알고리즘 ]

  1. 입력 받은 중위 표기식에서 토큰을 읽기

  2. 토큰이 피연산자면 토큰을 출력

  3. 토큰이 연산자(괄호 포함)일 때, 이 토큰이 스택의 top 연산자 보다 우선순위가 작을 때까지 스택에서 pop 한후 토큰의 연산자를 push 한다. 만약 top 에 연산자가 없으면 push 한다.

     (열린 괄호는 무조건 push, 닫힌 괄호는 열린 괄호를 만날 때까지 pop하여 연산자 출력하고 열린 괄호를 만나면 pop 만 하고 출력하지 않는다.)

     - 열린 괄호 우선순위 가장 높고 닫힌 괄호는 우선 순위가 가장 낮다.

  4. 이 과정을 반복하며 스택에 남아 있는 연산자를 모두 pop 하여 출력한다.

  

2. 후위 표기법의 수식을 스택을 이용하여 계산한다.

   ex) `2+3*4/5-6` -> `234*5/+6-`

   ex2) `5+4*(3-2*2)+7` -> `54322*-*+7+`

   1. 피연산자를 만나면 스택에 push한다.
   2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다.
   3. 수식이 끝나면 마지막으로 스택을 pop하여 출력한다.



### 연습문제 1

수식문자열을 읽어서 피연산자는 바로 출력하고 연산자는 스택에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop 하여 출력하시오. 연산자는 4칙 연산만 사용하시오.

예를 들어,  2 + 3 *  4 / 5 의 수식인 경우 2 3 4 * 5 /  +  가 출력되야한다.

```python
# My code

str_sentence = '2+3*4/5'
stack = []
ready_sentence = []

for i in str_sentence:

    if ord('1') <= ord(i) <= ord('9'):
        ready_sentence.append(i)
    else:
        if stack == []:
            stack.append(i)
        else:
            if i == '+' or i == '-':
                while stack:
                    ready_sentence.append(stack.pop[-1])
                stack.append(i)

            elif i == '*' or i == '/':
                while stack[-1] == '*' or stack[-1] == '/':
                    ready_sentence.append(stack[-1])
                    stack.pop(-1)
                stack.append(i)
while stack:
    ready_sentence.append(stack[-1])
    stack.pop(-1)

ready_sentence = ''.join(ready_sentence)

print(ready_sentence)
```



```python
# My code - 괄호 + 사칙연산 다 가능
str_sentence = input()
stack = []
ready_sentence = []

for i in str_sentence:
    if ord('1') <= ord(i) <= ord('9'):
        ready_sentence.append(i)

    else:
        if stack == []:
            stack.append(i)
        if '(' in stack:
            stack.append(i)
        if i == ')':
            stack.pop(-1)
            while '(' in stack:
                ready_sentence.append(stack[-1])
                stack.pop(-1)
            ready_sentence.pop(-1)

        if i == '(':
            stack.append(i)

        else:
            if (i == '+' or i == '-') and '(' not in stack:
                while len(stack)-1 >0:
                    ready_sentence.append(stack.pop(-1))


            elif (i == '*' or i == '/') and '(' not in stack:
                while stack[-1] == '*' or stack[-1] == '/':
                    ready_sentence.append(stack[-1])
                    stack.pop(-1)
                stack.append(i)
while stack:
    ready_sentence.append(stack[-1])
    stack.pop(-1)

ready_sentence = ''.join(ready_sentence)

print(ready_sentence)
```



## 백트래킹 ★★

문제를 푸는 과정 속에서 부분집합이나 순열이 포함되어 있을 때 만들어 보는 것이 백트래킹 상태공간 트리(선택의 과정, 답을 찾아가는 과정)를 이용하는 것이다!!!!

### 백트래킹이란?

- 해를 찾는 도중에(완전 탐색) 막히면(해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법

- 최적화 (optimization) 문제와 결정 (decision) 문제 해결 가능

  ex) 미로 찾기, n-Queen 문제, Map coloring, 부분 집합의 합(Subset Sum) 문제 등

#### 백트래킹 기법

최적화(완전 탐색이 우선!!!기본 접근 방법), 결정 문제 해결

- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모노드(이전의 선택)로 되돌아가 다음 자식 노드로 감
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.

#### 결정 문제

- 미로 찾기
- n-Queen 문제
- Map coloring
- 부분 집합의 합(Subset Sum) 문제 등

#### 구현 방법

- DFS - 일반적으로 효율적이기에 많이 사용
- BFS

#### 백트래킹과 깊이 우선 탐색의 차이

- 백트래킹

  - 문제 목적 : 최적해를 찾는 것, 빨리 찾는 것
  - prunning 가지치기를 통해 불필요한 경로 차단
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하여 처리 불가능.

- 깊이 우선 탐색 - 최적화 문제의 해결법, 그래프로 실제 탐색!!, 즉 그래프 문제이면 깊이 우선 탐색!

  - 그래프 문제 목적 : 모든 정점을 다 방문하는 것

  - 모든 경로 추적

  - 경우의 수 많음

    경우의 수가 너무 많아서  N!가지의 경우의 수를 가진 문제에 대해 처리 불가능.

#### 백트리킹 기법

- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 돌아가서(backtracking) 다음 자식 노드로 감
- 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며 반대로 해답의 가능성이 있으면 유망하다고 하낟.
- 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려X

#### 백트래킹 알고리즘 진행 절차

1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
2. 각 노드가 유망한지를 점검한다.
3. 만일 그 노드가 유망하지 않으면 그 노드의 부모 노드로 돌아가서 검색을 계속한다.

### 백트래킹 알고리즘

```python
def backtrack(a, k, input):
    if k == input:
        print(a)
    else:
        k += 1
        a[k] = 1
        backtrack(a, k, input)
        a[k] = 0
        backtrack(a, k, input)


a = [0] * 4
backtrack(a, 0, 3)
```

```python
# 출력
[0, 1, 1, 1]
[0, 1, 1, 0]
[0, 1, 0, 1]
[0, 1, 0, 0]
[0, 0, 1, 1]
[0, 0, 1, 0]
[0, 0, 0, 1]
[0, 0, 0, 0]
```

```python
# index = 0 부터
def backtrack(a, k, input):
    if k == input:
        print(a)
    else:
        a[k] = 1
        backtrack(a, k+1, input)
        a[k] = 0
        backtrack(a, k+1, input)


a = [0] * 4
backtrack(a, 0, 3)
```

#### 백트래킹 - 미로 찾기

미로 문제를 가지고 DFS, 백트래킹, 가지치기를 비교한다면, 엄격한 의미로 구분했을 때 기준입니다.

미로를 정의하고 만드는 건 DFS 미로에 길이 있는 지 여부를 찾아내는 건 백트래킹, 미로에서 가장 짧은 길을 찾아내는 건 백트래킹+가지치기

- 부분집합
  - 상태공간트리 = 선택의 과정
    - 원소의 수만큼 선택
    - 선택지 2가지

#### 부분집합 구하기

```python
# for 이용
# k: 함수호출의 깊이, n: 호출트리의 높이, 단말 노드
def subset(k, n): # k: 함수호출의 깊이, n: 호출트리의 높이, 단말 노드
    if k == n:
        pass
    else:
        for i in range(2):
            bit[k] = 0
            subset(k + 1, n)
subset(0, 3)

# 재귀 이용 -- 위의 for 이용한 코드와 같은 결과라는 것 이해하기
def subset(k, n):
    if k == n:
        print(bit)
    else:
        bit[k] = 0
        subset(k + 1, n)
        bit[k] = 1
        subset(k + 1, n)
subset(0, 3)
```

```python
# 부분집합 구하기
arr = 'ABC'
N = len(arr)
bit = [0] * N

for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i
            for j in range(N):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
            
# 출력
# 
# C 
# B 
# B C 
# A 
# A C 
# A B 
# A B C 
```

##### 재귀 + 비트 표현 --> 부분집합

```python
arr = 'ABC'
N = len(arr)
bit = [0] * N # 선택의 과정, 선택의 정보 저장

def subset(k, n):
    # k: 노드의 높이, n: 단일 노드의 높이
    # k: 지금까지 선택의 수, n: 해야할 선택의 수
    if k == n:
        pass
    else:
        # k번 요소를 포함하는 선택
        bit[k] = 1
        subset(k + 1, n)

        # k번 요소를 포함하지 않는 경우
        bit[k] = 0
        subset(k + 1, n)
subset(0, N)
```

##### 재귀 --> 부분집합

```python
# 부분집합의 개수 len 이용

arr = 'ABC'
N = len(arr)
A = []
def subset(k, n):
    # k: 노드의 높이, n: 단일 노드의 높이
    # k: 지금까지 선택의 수, n: 해야할 선택의 수
    if k == n:
        print(len(A), A)
    else:
        # k번 요소를 부분집합 포함
        A.append(arr[k])
        subset(k + 1, n)
        A.pop()

        # k번 요소를 포함하지 X
        subset(k + 1, n)
subset(0, N)

# 3 ['A', 'B', 'C']
# 2 ['A', 'B']
# 2 ['A', 'C']
# 1 ['A']
# 2 ['B', 'C']
# 1 ['B']
# 1 ['C']
# 0 []
```

```python
# 부분집합의 개수 cnt 이용

arr = 'ABC'
N = len(arr)
A = []
def subset(k, n, cnt):
    # k: 노드의 높이, n: 단일 노드의 높이
    # k: 지금까지 선택의 수, n: 해야할 선택의 수
    if k == n: # 종료 조건
        print(len(A), A)
    else:
        A.append(arr[k]) # k번 요소를 부분집합 포함
        subset(k + 1, n, cnt + 1)
        A.pop()
        
        subset(k + 1, n, cnt)  # k번 요소를 포함하지 X
subset(0, N, 0)

# 3 ['A', 'B', 'C']
# 2 ['A', 'B']
# 2 ['A', 'C']
# 1 ['A']
# 2 ['B', 'C']
# 1 ['B']
# 1 ['C']
# 0 []
```

##### 그룹 나누기

```python
arr = 'ABCD'; N = len(arr)

A, B = [], []
def subset(k, n):
    if k == n:
        print(A, B)
    else:
        # k번 요소를 부분집합 포함
        A.append(arr[k])
        subset(k + 1, n)
        A.pop()

        # k번 요소를 포함하지 X
        B.append(arr[k])
        subset(k + 1, n)
        B.pop()

subset(0, N)

# 출력
# ['A', 'B', 'C', 'D'] []
# ['A', 'B', 'C'] ['D']
# ['A', 'B', 'D'] ['C']
# ['A', 'B'] ['C', 'D']
# ['A', 'C', 'D'] ['B']
# ['A', 'C'] ['B', 'D']
# ['A', 'D'] ['B', 'C']
# ['A'] ['B', 'C', 'D']
# ['B', 'C', 'D'] ['A']
# ['B', 'C'] ['A', 'D']
# ['B', 'D'] ['A', 'C']
# ['B'] ['A', 'C', 'D']
# ['C', 'D'] ['A', 'B']
# ['C'] ['A', 'B', 'D']
# ['D'] ['A', 'B', 'C']
# [] ['A', 'B', 'C', 'D']


## 반으로 그룹 나누기
arr = 'ABCD'; N = len(arr)

A, B = [], []
def subset(k, n, cntA):
    if k == n:
        if cntA == N/2:
            print(A, B)
    else:
        # k번 요소를 부분집합 포함
        A.append(arr[k])
        subset(k + 1, n, cntA + 1)
        A.pop()

        # k번 요소를 포함하지 X
        B.append(arr[k])
        subset(k + 1, n, cntA)
        B.pop()

subset(0, N, 0)
# ['A', 'B'] ['C', 'D']
# ['A', 'C'] ['B', 'D']
# ['A', 'D'] ['B', 'C']
# ['B', 'C'] ['A', 'D']
# ['B', 'D'] ['A', 'C']
# ['C', 'D'] ['A', 'B']

## 중복제거 --> 하나 미리 박아놓으면 된다.
arr = 'ABCD'; N = len(arr)

A, B = [], []
def subset(k, n, cntA):
    if k == n:
        if cntA == N/2:
            print(A, B)
    else:
        # k번 요소를 부분집합 포함
        A.append(arr[k])
        subset(k + 1, n, cntA + 1)
        A.pop()

        # k번 요소를 포함하지 X
        B.append(arr[k])
        subset(k + 1, n, cntA)
        B.pop()
A.append(arr[0])
subset(1, N, 1)

# ['A', 'B'] ['C', 'D']
# ['A', 'C'] ['B', 'D']
# ['A', 'D'] ['B', 'C']
```



### 연습문제 2

{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powersest 중 원소의 합이 10인 부분집합을 구하시오.

```python
# 부분집합 찾기
def backtrack(a, k, input):
    if k == input:
        for i in range(input):
            if a[i]: print(S[i], end='')
        print()
    else:
        a[k] = 1
        backtrack(a, k+1, input)
        a[k] = 0
        backtrack(a, k+1, input)


a = [0] * 10
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(a, 0, 10)
```

```python
# 부분집합 합찾기
def backtrack(a, k, input):
    if k == input:
        psum = 0
        for i in range(input):
            if a[i]: psum += S[i]
        if psum == 10:
            for i in range(input):
                if a[i]: print(S[i], end='')
            print()
    else:
        a[k] = 1
        backtrack(a, k+1, input)
        a[k] = 0
        backtrack(a, k+1, input)


a = [0] * 10
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(a, 0, 10)
```

```python
# 최종 solution

def backtrack(a, k, input, s):
    if s > 10: return # 가지치기_10 넘어가면 바로 넘어감

    if k == input:
        if s == 10:
            for i in range(input):
                if a[i]: print(S[i], end=' ')
            print()
    else:
        a[k] = 1
        backtrack(a, k+1, input, s + S[k])
        a[k] = 0
        backtrack(a, k+1, input, s)


a = [0] * 10
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(a, 0, 10, 0)
```

### 순열

#### 1. `if문` 이용

```python
arr = 'ABC'; N = len(arr)
for i in range(N):
    for j in range(N):
        if j == i: continue
        for k in range(N):
            if k == i or j == k: continue
            print(arr[i], arr[j], arr[k])
```

#### 2. list 이용 

```python
arr = 'ABC'; N = len(arr)
order = [] # 순서를 기록하는 리스트
for i in range(N):
    order.append(arr[i])
    for j in range(N):
        if arr[j] in order: continue
        order.append(arr[j])
        for k in range(N):
            if arr[k] in order: continue
            order.append(arr[k])
            print(order)
            order.pop()
        order.pop()
    order.pop()
```

#### 3. 재귀함수 이용

```python
# 1.
arr = 'ABC'; N = len(arr)
order = []
def perm(k, n):
    if k == n:
        print(order)
    else:
        for i in range(N):
            if arr[i] in order: continue
            order.append(arr[i])
            perm(k + 1, n)
            order.pop()
perm(0, N)

# 2.
arr = 'ABC'; N = len(arr)

order = []
visit = [0] * N
def perm(k, n):
    if k == n:
        print(order)
    else:
        for i in range(N):
            if visit[i]: continue
            visit[i] = 1; order.append(arr[i])
            perm(k + 1, n)
            visit[i] = 0; order.pop()
perm(0, N)

# 3, 비트
arr = 'ABC'; N = len(arr)

order = []
visit = [0] * N
def perm(k, n, visit):
    if k == n:
        print(order)
    else:
        for i in range(N):
            if visit & (1<<i): continue
            order.append(arr[i])
            perm(k + 1, n, visit | (1 << i))
            order.pop()
perm(0, N, 0)
```



## 분할정복 ★

### 설계 전략

- 분할 (Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
- 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
- 통합(Combine) : (필요하다면) 해결된 해답을 모은다. _ 퀵은 필요X, 합병정렬 필요

 

### 퀵정렬

부할 할 때 기준 아이템 (**pivot** item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치

정렬의 안정성을 보장하지는 못함. 평균 시간복잡도으로는 좋은 정렬임.

cf) 합병정렬(merge sort) : 그냥 두 부분으로 나눔, 각 부분 정렬이 끝난 후 `합병`이라는 후처리 작업 필요! (퀵정렬은 필요X)



### 퀵정렬 알고리즘

```python
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R) : L += 1
        while(a[R] >= a[pivot] and L < R) : R -= 1
        if L < R:
            if L == pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pibot], a[R] = a[R], a[pibot]
    return R
```

```python
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R) : L += 1
        while(a[R] >= a[pivot] and L < R) : R -= 1
        if L < R:
            if L == pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)


a = [69, 10, 30, 2, 16, 8, 31, 22]
quickSort(a, 0, len(a)-1)
print(a)
```



