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

