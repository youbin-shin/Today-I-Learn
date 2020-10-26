## Chapter9. 힙

2020.10.26

## Heap 이란?

- 특정한 규칙을 갖는 트리
- 우선순위 큐를 위해 만들어진 구조
- 최솟값, 최댓값을 찾는 연산을 하기 위한 완전 이진 트리의 기본

- heap property
  - 최소힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
  - 최대힙 : 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

### 사용방법

```python
import heapq
```

#### method 정리

- heapq`.heapify(배열이름)` : 기존 배열을 Heap 구조로 생성
- heapq`.heappush(배열이름, 요소)` : Heap에 요소 추가
- heapq`.heappop(배열이름)` : Heap 요소를 삭제
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

