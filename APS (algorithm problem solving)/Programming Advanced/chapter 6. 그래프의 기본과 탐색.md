# chapter 6. 그래프의 기본과 탐색

2020.05.21

### 학습 목표

- 실 세계 문제를 그래프로 추상화해서 해결하는 방법을 학습한다.
  - 그래프 탐색 기법인 BFS와 DFS에 대해 학습한다.
  - 그래프 알고리즘에 활용되는 상호배타 집합(Disjoint-Sets)의 자료구조에 대해 학습한다.
  - 최소 신장 트리(Minimum Spanning Tree)를 이해하고 탐욕 기법을 이용해서 그래프에서 최소 신장 트리를 찾는 알고리즘을 학습한다.
  - 그래프의 두 정점 사이의 최단 경로(Shortest Path)를 찾는 방법을 학습한다.

---

## 그래프 기본

### 그래프

- 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현한다.

- 그래프 : **정점(Vertex)**들의 집합과 이들을 연결하는 **간선(Edge)**들의 집합으로 구성된 자료 구조

  - IVI : 정점의 개수, IEI : 그래프에 포함된 간선의 개수

  - IVI 개의 정점을 가지는 그래프는 최대 IVI(IVI - 1) / 2 간선이 가능

    ex) 5개 정점이 있는 그래프의 간선 수는 10 (= 5 * 4 / 2) 개이다.

- 선형 자료구조(리스트, 배열)나 트리 자료구조로 표현하기 어려운 **N : N 관계**를 가지는 원소들을 표현하기에 용이하다.

#### 그래프 유형

- 무향 그래프 (Undirected Graph) : 간선의 방향성 X

- 유향 그래프 (Directed Graph) : 간선의 방향성 O

- 가중치 그래프 (Weighted Graph) : 간선에 가중치 부여 필요

- 사이클 없는 방향 그래프 (DAG, Directed Acyclic Graph) 

  - ex) 트리
  - 사이클 : 시작 정점과 끝 정점이 같은 단순 경로

  ---

- 완전 그래프 : 정점들에 대해 가능한 모든 간선들을 가진 그래프

- 부분 그래프 : 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프, Sub Graph

#### 인접 정점

- 인접 (Adjacency)
  - 두 개의 정점에 간선이 존재(연결됨)하면 서로 인접해 있다고 한다.
  - 완전 그래프에 속한 임의의 두 정점들은 모두 인접해 있다.

#### 그래프 경로

- 경로란 간선들을 순서대로 나열한 것
  - 간선들 : (0, 2), (2, 4), (4, 6)
  - 정점들 : 0 - 2 - 4 - 6
- 경로 중 한 정점을 최대한 한번만 지나는 경로를 `단순 경로`라 한다.
  - 0 - 2 - 4 - 6, 0 - 1 - 6
- 시작한 정점에서 끝나는 경로를 `사이클(Cycle)`이라 한다.
  - 1 - 3 - 5 - 1

### 그래프 표현 :star:

간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정

- **인접 행렬 (Adjacent matrix)**
  - IVI X IVI 크기의 2차원 배열(정방 행렬)을 이용해서 간선 정보를 저장
  - 배열의 배열 (포인터 배열)
- **인접 리스트 (Adjacent List)**
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- **간선의 배열**
  - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

#### 인접 행렬

두 정점을 연결하는 간선의 유무를 행렬로 표현

- 행 번호와 열 번호는 그래프의 정점에 대응

- 두 정점이 인접해 있으면 1, 그렇지 않으면 0으로 표현

  ---

- 무향 그래프 : i 번째 행의 합 = i 번째 열의 합 = Vi의 차수(Vi 정점에 연결된 정점의 수)

- 유향 그래프

  - 행 i의 합 = Vi의 진출 차수
  - 열 i의 합 = Vi의 진입 차수

  ---

- 단점

  간선이 적더라도 V * V 크기의 공간 확보 => 효율이 떨어지고 메모리 차지

  인접 정점을 찾을 때 인접 정점이 적더라도 V 번 연산 필요

#### 인접 리스트

각 정점에 대한 인접 정점들을 순차적으로 표현

- 하나의 정점에 대한 인접 정점들을 각각 노드로 하는 연결 리스트로 저장

  ---

- 무향 그래프

  - 노드 수 = 간선의 수 * 2
  - 각 정점의 노드 수 = 정점의 차수

- 유향 그래프

  - 노드 수 = 간선의 수
  - 각 정점의 노드 수 = 정점의 진출 차수

  ---

- 단점

  진입 차수를 구하기 위해서는 V 만큼 찾아 봐야한다. 

  진입 차수 관련 문제는 인접 행렬이 유리하다.

### 문제 제시: 친구관계

- A로 부터 시작해서 한 명의 친구에게만 소식을 전달, 전달 할 수 있다면 최대 몇 명의 친구가 소식을 받을 수 있을까? (단, 소식을 전달받은 친구한테는 소식을 재전달할 수 없다.) `DFS`

- A로 부터 시작해서 친구들에게 동시에 소식을 전달할 수 있다고 할 때, 가장 늦게 전달받는 사람은 누구일까? (단 친구에게 소식을 전달하는 속도는 동일하다.) `BFS`

  ---

- A의 친구는 B다.
- C의 친구는 E, F이다.
- (D - F), (F - G), (N - B, I, L), (G - A, C, D, H), (I - J, H), (B - D, K, L), (M - I, J), (E - A, H), (C - B, I, L), (B - I), (J - A, G)
- A의 친구 중에 친구가 가장 많은 친구는 누구인가?

---

## 그래프 순회 (탐색)

그래프 순회는 비선형구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미한다.

- 방법
  - 깊이 우선 탐색 (Depth First Search, DFS)
  - 너비 우선 탐색 (Breadth First Search, BFS)

### 깊이 우선 탐색 (Depth First Search, DFS)

시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색하다가 갈 곳 없으면 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하다 결국 모든 정점을 방문하는 순회방법

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반족해야 하므로 **후입선출 구조**의 **`스택`** 사용

#### 스택 (stack)

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료 구조
- 선형 구조 : 자료 간의 관계가 1 대 1의 관계를 갖는다.
  - cf) 비선형 구조 : 자료 간의 관계가 1 대 N 의 관계를 갖는다. (ex) 트리

- 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
  - 후입선출 (LIFO, Last-In-First-Out)

##### 스택의 구현

스택을 구현하기 위해서 필요한 저장소와 연산

- 자료를 선형으로 저장할 저장소

  - C언어에서는 배열을 사용할 수 있다.
  - 저장소 자체를 스택이라 부르기도 한다.
  - **스택에서 마지막 삽입된 원소의 위치**를 `top`이라 부른다.

- 연산

  |  연산   | 역할                                           |
  | :-----: | ---------------------------------------------- |
  |  push   | 저장소에 자료를 삽입(저장)한다.                |
  |   pop   | 저장소에서 자료를 꺼낸다. (삽입한 자료의 역순) |
  | isEmpty | 스택이 공백인지 아닌지를 확인하는 연산         |
  |  peek   | 스택의 top에 있는 item(원소)을 반환하는 연산   |

  - push 알고리즘 :  top을 1 더하고 스택에 넣어준다.
  - pop 알고리즘 : 자료가 있다면 top을 줄이고 top+1한 값을 return 한다.

#### DFS 알고리즘 - 재귀

```python
# 입력
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, V+1):
        if adj[v][i] == 1 and visited[i] == 0:
            dfs(i)


V, E = map(int, input().split())
edges = list(map(int, input().split()))

# 인접 행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    # 무향 그래프
    adj[s][e] = 1
    adj[e][s] = 1
    
visited = [0]*(V+1)
dfs(1) # 1 2 4 6 5 7 3
```

#### DFS 알고리즘 - 반복 (스택 이용)

```python
# 입력
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs_stack(v):
    s = []
    top = -1
    visited = [0] * (V + 1)
    s.append(v)
    while s:
        u = s.pop()
        if visited[u] == 0:
            print(u, end=' ')
            visited[u] = 1
            for i in range(1, V+1):
                if adj[u][i] == 1 and visited[i] == 0:
                    s.append(i)


V, E = map(int, input().split())
edges = list(map(int, input().split()))

# 인접 행렬
adj = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    # 무향 그래프
    adj[s][e] = 1
    adj[e][s] = 1


dfs_stack(1) # 1 3 7 6 5 2 4 
```

### 너비 우선 탐색 (Breadth First Search, BFS)

탐색(모든 원소를 순회!) **시작점의 인접한 정점들을 먼저 모두** 차례로 방문한 후에 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, **선입선출** 형태의 자료구조인 **`큐`**를 활용함
- 최단 거리문제들에 사용되는 알고리즘

#### 큐 Queue

#### 큐의 특성

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
  - 큐의 뒤에는 삽입만!
  - 큐의 앞에서는 삭제만!
- 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제된다. (ex. 맛집 줄서기)
  - 선입선출 구조 (FIFO: First In First Out)
    - 머리 `Front` : 저장된 원소 중 첫번째 원소
    - 꼬리 `Rear` : 저장된 원소 중 마지막 원소

#### 큐의 기본 연산

##### 삽입 `enQueue(item)`

마지막 원소 뒤에 새로운 원소를 삽입하기 위해 (큐가 꽉차지 않았다면!)

1. **rear 값을 하나 증가**시켜 새로운 원소를 삽입할 자리를 마련
2. 그 인덱스에 해당하는 배열원소 **Q[rear]에 item을 저장**

##### 삭제 `deQueue`

가장 앞에 있는 원소를 삭제하기 위해 (큐가 비어있지 않다면!)

1. **front 값을 하나 증가**시켜 큐에 남아있게 될 첫번째 원소 이동
2. 새로운 첫번째 원소를 **리턴**함으로써 삭제와 동일한 기능

#### 공백 상태 `isEmpty()`  및 포화 상태 검사 `isFull()`

- 공백 상태 : front = rear
- 포화 상태 : rear = n - 1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)

#### 큐의 연산 과정

1. 공백 큐 생성 `createQueue()`

   큐 초기화 : front = rear = -1

2. 원소 A 삽입 `enQueue(A)`

   rear += 1

   Q[rear] = A

3. 원소 B 삽입  `enQueue(B)`

   rear += 1

   Q[rear] = B

4. 원소 반환/삭제 `deQueue()`

   front += 1

   return Q[front]

5. 원소 C 삽입  `enQueue(B)`

   rear += 1

   Q[rear] = C

6. 원소 반환/삭제 `deQueue()`

   front += 1

   return Q[front]

7. 원소 반환/삭제 `deQueue()`

   front += 1

   return Q[front] => **front = rear** "큐가 비어있다!"

#### 연습문제 BFS

입력값은 정점과 간선 정보가 주어지고 이어서 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다. 모든 정점을 너비 우선 탐색하여 경로를 출력하시오. 시작 정점은 1로 시작하시오. 

```python
# 입력
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def bfs(v):
    q = []
    visited = [0]*(V+1)
    q.append(v)
    visited[v] = 1
    while q:
        u = q.pop()
        print(u, end=' ')
        for w in adj[u]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1


V, E = map(int, input().split())
ed = list(map(int, input().split()))
# 인접리스트
adj = {i: [] for i in range(1, V+1)}
for i in range(E):
    s, e = ed[2*i], ed[2*i+1] # 간선 시작, 간선 끝
    # 무방향
    adj[s].append(e)
    adj[e].append(s)
# print(adj)
# 인접리스트 : {1: [2, 3], 2: [1, 4, 5], 3: [1, 7], 4: [2, 6], 5: [2, 6], 6: [4, 5, 7], 7: [6, 3]}

bfs(1) # 1번 정점부터 bfs 시작
# 출력 : 1 3 7 6 5 4 2 
```

---

## 서로소 집합들 (Disjoint-Sets)

**서로소** 또는 **상호배타 집합**들은 서로 중복 포함된 원소가 없는 집합들 (교집합 X)

- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분한다. => `대표자(representative)`
- 상호배타 집합 표현 방법
  - 연결 리스트
  - 트리

### 상호배타 집합 연산

- `Make-Set(x)` : 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

- `Find-Set(x)` : x를 포함하는 집합을 찾는 연산

- `Union(x, y)` : x와 y를 포함하는 두 집합을 통합하는 연산

### 상호배타 집합 표현 - `연결리스트`

- 같은 집합의 원소들은 하나의 연결리스트로 관리한다.
- 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼는다.
- 각 원소는 집합의 대표원소를 가리키는 링크를 갖는다.

### 상호배타 집합 표현 - `트리`

- 하나의 집합(a disjoint set)을 하나의 트리로 표현한다.
- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 된다.

```python
def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x: return x
    else: return find_set(p[x])


def union(x, y):
    p[find_set(y)] = find_set(x)

N = 6
p = [0] * (N+1)
for i in range(1, N+1):
    make_set(i)
# print(p) [0, 1, 2, 3, 4, 5, 6]
union(1, 3)
union(2, 3)
union(5, 6)
print(p) # [0, 2, 2, 1, 4, 5, 5]
print(find_set(6)) # 5
# 출력 : [0, 2, 2, 1, 4, 5, 5]
```

- 문제점

  대표자를 찾기 위해 재귀호출 여러번 실행

- 해결 방법

  대표자를 바로 찾아가도록 `path compression`

#### 연산의 효율 높이는 방법

##### Rank를 이용한 Union

- 각 노드는 자신을 루트로 하는 subtree의 높이를 Rank라는 이름으로 저장한다.
- 두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙인다.
  - rank가 같은 경우 합쳐준 뒤 rank +1 해준다.

```python
def make_set(x):
    p[x] = x
    # rank[x] = 0
    
def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x]) # 대표자 값으로 갱신
        return p[x]


def union(x, y):
    px = find_set(x) # x의 대표자
    py = find_set(y) # y의 대표자
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


N = 8
p = [0] * (N+1)
rank = [0] * (N+1)
for i in range(1, N+1):
    make_set(i)

union(1, 3)
union(2, 3)
union(5, 6)
union(6, 8)
union(1, 5)
union(6, 7)
print(p) # [0, 3, 3, 6, 4, 6, 6, 6, 6]
print(find_set(4)) # 4
print(find_set(5)) # 6
```

![image-20210117225946938](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20210117225946938.png)

![image-20210117230002021](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20210117230002021.png)

##### Path compression

Find-Set을 행하는 과정에서 만나는 모든 노드들이 **직접 root(`대표자`)**를 가리키도록 포인터(부모를 갱신)를 바꾸어 준다.

```python
def find_set(x): # path compression
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    p[find_set(x)] = find_set(y)


N = 8
p = [i for i in range(N+1)] # make_set
```

