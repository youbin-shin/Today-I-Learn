# chapter 6. 큐 (BFS)

> 2020.04.03

### BFS(Breadth First Search)

> 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

#### 그래프 탐색하는 방법

두 경우 모두 완전 탐색 알고리즘

주어진 문제가 끝까지 가는 게 주요 핵심이면 DFS, 같은 거리/레벨 만큼 가는 것이 중요하다면 BFS!

1. 깊이 우선 탐색(Depth First Search, DFS)
   - 재귀
     - 재귀 호출이 스택의 역할을 대신함. (스택 제어 필요 X)
     - 구현이 간단해짐!
   - 반복 --> 스택
2. 너비 우선 탐색 (Breadth First Search, BFS)
   - 최단 거리에 특화된 편
   - 재귀로 구현 가능하나 DFS처럼 재귀의 이점이 X

##### 그래프 표현 방법

- 인접 행렬
- 인접 리스트
  - 인접 행렬의 메모리 낭비를 줄이기 위한 구현 방법
- 간선 배열
  - 시작 정점과 끝 정점의 정보 저장

#### 너비 우선 탐색 특징

- 인접한 정점들에 대해 탐색을 한 후, 차레로 다시 너비우선 탐색을 진행해야 하므로, 선입선출 형태의 자료 구조인 큐를 활용함.

#### BFS 알고리즘

입력 파라미터 : 그래프 G 와 탐색 시작점 v

```python
def BFS(G, v):
    # 초기화, 준비단계
    visited = [0] * n # 중복 방문 방지, 정점의 개수
    queue = [] # 큐 생성
    queue.append(v) # 시작점 v를 큐에 삽입
    visited[v] = True # 방문으로 표시
    
    while queue: # 큐가 비어있지 않은 경우
        t = queue.pop(0) # 큐의 첫번째 원소 반환
    	visit(t) # t 노드에 대해 할 일(문제별로 달라짐!)
        for i in G[t]: # t와 연결된 모든 선에 대해
            if not visited[i]: 
                queue.qppend(i) # 방문하지 않은 정점 큐에 넣기
                visited[i] = True         
                ## visited[i] = visited[t] + 1 (거리 정보)
```

##### 초기 상태

- visited 배열 초기화
- Q 생성
- 시작점 enqueue

### 연습문제 3

모든 정점을 너비우선탐색하여 경로를 출력하시오. 시작 정점을 1로 시작하시오.

![image-20200403102015679](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200403102015679.png)

```python
# input: 1, 2, 1, 3, 2, 34, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

```

![image-20200403103518267](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200403103518267.png)

### 