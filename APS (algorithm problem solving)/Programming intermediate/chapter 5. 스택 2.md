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

### 백트래킹이란?

해를 찾는 도중 막히면 즉 해가 아니면 되돌아가서 다시 해를 찾아 가는 기법

최적화 (optimization) 문제와 결정 (decision) 문제 해결 가능

ex) 미로 찾기, n-Queen 문제, Map coloring, 부분 집합의 합(Subset Sum) 문제 등



- 백트래킹과 깊이 우선 탐색의 차이

  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임. (Prunning 가지치기)

  - 깊이 우선 탐색이 모든 경로를 추적하지만 백트래킹은 불필요한 경로를 조기에 차단.

  - 깊이 우선 탐색은 경우의 수가 너무 많아서  N!가지의 경우의 수를 가진 문제에 대해 처리 불가능.

  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하여 처리 불가능.

    

- 백트리킹 기법

  - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 돌아가서(backtracking) 다음 자식 노드로 감
  - 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며 반대로 해답의 가능성이 있으면 유망하다고 하낟.
  - 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려X
  - **알고리즘 절차**
    1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
    2. 각 노드가 유망한지를 점검한다.
    3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.



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



