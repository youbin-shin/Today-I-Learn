# chapter 7. 그래프의 최소 비용 문제

## 최소 신장 트리 (MST)

- 그래프에서 최소 비용 문제 유형

  1. 모든 정점을 연결하는 간선들의 **가중치**의 합이 **최소**가 되는 트리 `MST`

     - MST 알고리즘

       프림 : `정점` 기준

       크루스칼 : `간선` 기준

  2. 두 정점 사이의 최소 비용의 경로 찾기 `최단 거리`

     - 최단거리 문제는 이전까지 BFS로 풀었다! => 가중치가 있다면 `최단거리`

- 신장 트리

  n 개의 정점으로 이루어진 무방향 그래프에서 n 개의 정점과 n-1개의 간선으로 이루어진 트리

- 최소 신장 트리 (Minimum Spanning Tree)

  무방향 **가중치** 그래프에서 신장 트리를 구성하는 간선들의 합이 최소인 신장 트리

### MST 표현

=> 그래프 표현 + **가중치** 값

- 인접 행렬

- 인접 리스트

  ---

- 그래프
- 간선들의 배열
- 인접 리스트
- 부모 자식관계와 가중치에 대한 배열
  - 트리

### Prim 알고리즘

- **하나의 정점**에서 연결된 간선들 중에서 하나씩 선택하면서 MST를 만들어 가는 방식
  1. 임의 정점을 하나 선택해서 시작
  2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
  3. 모든 정점이 선택될 때까지 1, 2번 과정 반복
- 서로소인 2개의 집합 (2 disjoint-sets) 정보를 유지
  - `트리 정점들` (tree vertices) : MST 를 만들기 위해 선택된 정점들
  - `비트리 정점들` (nontree vertices) : 선택되지 않은 정점들

#### 알고리즘 기본 과정

1. key = 무한대, pi =  none/-1 로 초기화

2. 시작 정점 -> key[시작점] = 0

3. 아직 MST가 아니면서 key 가 최소인 정점 선택 => u

4. u를 MST로 선택

5. u에 인접하고 MST가 아직 아닌 정점 w

   key[w] > u-w 가중치 인 경우 갱신

6. 3 ~ 5계속 반복

![image-20200522101735466](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200522101735466.png)

#### 코드 구현

```markdown
입력 예시 값
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

출력
[0, 21, 31, 34, 46, 18, 25]
```

##### 인접행렬 이용

```python
V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)] # 인접행렬
for i in range(E):
    s, e, c = map(int, input().split()) # 시작정점, 끝정점, 가중치
    adj[s][e] = c
    adj[e][s] = c

# key, p, mst 준비
INF = float('inf')
key = [INF] * V
p = [-1] * V
mst = [False] * V

# 시작점 선택 : 0번 선택
key[0] = 0 # 시작 key : 0
cnt = 0
result = 0
while cnt < V :
    # 아직 mst가 아니고 key가 최소인 정점 선택 : u
    min = INF # 초기화
    u = -1 # 초기화
    for i in range(V):
        if not mst[i] and key[i] < min:
            min = key[i]
            u = i
    # u를 mst로 선택
    mst[u] = True
    result += min # 최소 가중치, 누적합
    cnt += 1
    # key 값을 갱신
    # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
    for w in range(V):
        if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
            key[w] = adj[u][w]
            p[w] = u

print(key) # [0, 21, 31, 34, 46, 18, 25]
print(p) # [-1, 2, 0, 4, 2, 3, 2]
print(result) # 175
```

##### 인접리스트 + 우선순위 큐 이용

```python
import heapq

V, E = map(int, input().split())
adj = {i:[] for i in range(V)} # 인접리스트
for i in range(E):
    s, e, c = map(int, input().split()) # 시작정점, 끝정점, 가중치
    adj[s].append([e, c])
    adj[e].append([s, c])

# key, mst, 우선순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []

# 시작점 선택 : 0번 선택
key[0] = 0
# 큐에 시작정점을 넣는다! (key, 정점인덱스)
# 우선순위 큐 -> 이진힙 -> library : heapq
heapq.heappush(pq, (0, 0)) # 우선순위 큐(원소의 첫번재 요소) : key를 우선순위로
result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq) # 가장 작은값 꺼낸다. (key, u)
    if mst[node] : continue # old 한 정보면 스킵
    # mst로 선택
    mst[node] = True
    result += k
    # key 값을 갱신 => key 배열/큐
    for dest, wt in adj[node]: # dest 가고자하는 곳, wt 가중치
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 (필요없는 원소는 스킵)
            heapq.heappush(pq, (key[dest], dest))

print(result) # 175
```

### KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘

  1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬

  2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴

     - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택

       사이클 존재 여부 파악 조건? 선택된 두 정점의 대표자가 같으면!

  3. **n - 1** 개의 간선(정점다 연결!)이 선택될 때까지 2를 반복

#### 구현한 코드

```python
def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(E)]
# print(edges)

# 간선을 간선가중치를 기준으로 정렬
edges.sort(key=lambda x:x[2]) # x의 두번째를 기준으로 정렬한다.
# print(edges)
# make_set : 모든 정점에 대해 집합 생성
p = [0] * V
rank = [0] * V
for i in range(V):
    make_set(i)

cnt = 0
result = 0
mst = []
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지
for i in range(E):
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
    # 사이클이면 스킵 : 간선의 두 정점이 서로 같은 집합이면 => "find_set"
    if find_set(s) == find_set(e): continue
    # 간선 선택 => mst에 간선 정보 더하기 / 두 정점을 합친다 "union"
    result += c
    mst.append(edges[i])
    union(s, e)

    cnt += 1
    if cnt == V -1 : break
print(result) # 175
print(mst) # [[3, 5, 18], [1, 2, 21], [2, 6, 25], [0, 2, 31], [3, 4, 34], [2, 4, 46]]
```

#### 연습문제

```markdown
입력값 (간선정보, 가중치) 랜덤하게 받음 
0 1 2
0 2 2
0 5 8 
1 2 1
1 3 19
2 5 5
3 4 7
3 5 11
3 6 15
4 5 9
4 6 3
```

![image-20200522150010057](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200522150010057.png)

## 최단 경로

### 최단 경로란?

간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로

- cf) 간선 가중치가 균일(1)할 때 `BFS` 이용

#### 알고리즘

- 하나의 시작 정점에서 끝정점까지의 최단 경로

  "one to all" 에서 타겟으로 하는 것을 선택

  - `다익스트라(dijkstra)` 알고리즘 :dart:

    음의 가중치를 허용 X

    - 음의 가중치는 사이클이 만들어 지면 무한대가 되기 때문!

  - `벨만-포드(Bellman-ford)` 알고리즘 : 음의 가중치 허용

- 모든 정점들에 대한 최단 경로

  - `플로이드-워샬(Floyd-Warshall)` 알고리즘

### Dijkstra 알고리즘

시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식

- 시작정점 (s) 에서 끝 정점 (t) 까지의 최단 경로에 정점 x가 존재한다.

  `s => x` , `x => t`

- 이때, 최단 경로는 `s에서 x까지의 최단 경로`와 `x에서 t까지의 최단 경로`로 구성된다.

- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사하다.

![image-20200522152156936](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200522152156936.png)

d[정점] : 시작점부터 정점까지의 거리 (현재까지 알아낸 최단)

![image-20200522152345765](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200522152345765.png)

#### 구현된 코드 (다익스트라 + 인접리스트)

```markdown
입력 
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6

출력
[0, 3, 5, 9, 11, 12]
```

```python
# dist, selected 배열 준비
# 시작점 선택
# 모든 정점이 선택될 때까지
# 아직 선택되지 않고 dist 의 값이 최소인 정점 : u
# 정점 u의 최단거리 결정
# 정점 u에 인접한 정점에 대해서 간선완화
V, E = map(int, input().split())
adj = {i: [] for i in range(V)} # 인접리스트
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c]) # 단방향이기에

INF = float('inf')
dist = [INF] * V
selected = [False] * V

dist[0] = 0
cnt = 0
while cnt < V:
    # dist 가 최소인 정점 찾기
    min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < min:
            min = dist[i]
            u = i
    # 결정
    selected[u] = True
    cnt += 1
    # 간선완화
    for w, cost in adj[u]: # 도착정점 w, 가중치 cost
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost

print(dist) # [0, 3, 5, 9, 11, 12]
```

