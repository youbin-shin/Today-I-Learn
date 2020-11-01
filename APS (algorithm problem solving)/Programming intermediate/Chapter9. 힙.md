## Chapter9. 힙

2020.10.26

## Heap 이란?

### 힙 구조

- 정의

  - 완전 이진 트리에 가까운 형태
    - 이진 트리 : 각 노드의 자식수가 2이하인 경우
    - 완전 이진 트리 : Root 노드 부터 Leaf 노드까지 빠짐업숴져 있는 트리
  - 특정한 규칙을 갖는 트리
  - 우선순위 큐를 위해 만들어진 구조

- 힙 특성

  - 최대힙 특성 (Max-Heap Property)

    부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

    Root 노드 값이 가장 큼

  - 최소힙 특성 (Min-Heap Property)

    부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙

    Root 노드 값이 가장 작음

- #### 알고리즘 Tip

  - 트리 형태를 배열로 저장하기에 다음과 같이 검색 가능하다.

    배열의 i 인덱스의 부모는` i / 2` 의 값의 인덱스를 갖는다!

    즉 i라는 노드의 왼쪽 자식은 2 * i, 오른쪽 자식은 2 * i + 1로 조회할 수 있다.

  - 노드의 높이

    : 현재 노드에서 leaf 노드까지 내려갈 때 가장 단순하게 내려가는 가장 긴 경로(simple path)에서 거쳐야하는 간선의 수

    `높이 h = log(n)`

    완전 이진 트리 구조를 가지지 때문이다.

#### 힙 정렬 (Heap Sort)

- 시간복잡도 : O(nlogn) 
  - 합병정렬과 동일

- 힙 구조의 특성을 이용한 정렬
- 삽입 정렬과 동일한 제자리 정렬 (Sort in Place)



### 사용방법

```python
import heapq
```

#### method 정리

- heapq`.heapify(배열이름)` : 기존 배열을 Heap 구조로 생성
- heapq`.heappush(배열이름, 요소)` : Heap에 요소 추가
- heapq`.heappop(배열이름)` : Heap에서 가장 작은 원소를 삭제 후 값을 리턴
- heapq`.heappushpop(배열이름, 요소)` : 요소를 푸시한 다음 heap에서 가장 작은 항목을 pop 하여 반환하기
  - heappush() 후 heappop()을 별도로 호출하는 것보다 더 효율적으로 실행
- heap`.heapreplace(배열이름, 요소)` : heap에서 가장 작은 요소 반환, 새로운 요소 푸쉬
  - 힙이 비어있으면 IndexError 발생

```python
import heapq

# heapify
a = [1, 4, 2, 5, 6, 8, 0]
heapq.heapify(a)
print(a) # [0, 4, 1, 5, 6, 8, 2]

# heappush
heapq.heappush(a, -2)
print(a) # [-2, 0, 1, 4, 6, 8, 2, 5]

# heappop
heapq.heappop(a)
print(a) # [0, 4, 1, 5, 6, 8, 2]
```

#### 최소 힙

```python
import heapq

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap) # 출력 : [1, 3, 5, 4, 8, 7]
```



#### 최대 힙

n : 하위 트리의 노드의 개수

- 노드의 값을 바꿀 때 수행시간 : O(n)
- 힙의 높이 O(h) = O(logn)
- 수행시간 : O(logn)

```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1], end=" ")  # 출력 : 8 7 5 4 3 1
```

