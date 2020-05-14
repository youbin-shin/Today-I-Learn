# chapter 4. 분할정복 & 백트래킹

2020.05.04

> 학습목표
>
> - 문제를 분할해서 핵5ㅕㄹ하는 분할 정복 (Divide and Conquer) 기법을 이해하고 대표적인 알고리즘인 퀵 정렬과 병합 정렬에 대해 학습한다.
> - 상태 공간 트리의 모든 노드를 검색하는 백트래킹에 대해 학습한다.
> - 이진 트리(Binary Tree)의 특성을 이애하고 이진 트리의 중요한 연산인 탐색, 삽입, 삭제 알고리즘을 학습한다.

### 분할정복

#### 문제 제시 : 가짜 동전 찾기

- n 개의 동전들 중 가짜 동전이 하나 포함되어 있다. 가짜 동전은 진짜 동전에 비해 아주 조금 가볍다. 진짜 동전들의 무게가 동일하다고 할 때 양팔저울을 이용해서 가짜 동전을 찾아보자.

  양팔 저울을 최소로 사용해서 가짜 동전을 찾는 방법은 무엇인가? 예를 들어 동전이 24개(진짜 23개, 가짜 1개)있다면?

  ---

- 평균 구하기

  하나하나 비교할 때 24개의 동전이 있다면  최소 1번부터 최대 12번 비교할 것이다.

  평균을 구해보면 12 * 13 / 2 * ( 1/12 ) = 6.5 이다.

  즉 n 개의 동전이 있다면 경우의 수는 1 ~ n/2 이고 평균은 ((n/2) * (n/2 + 1))/2 * (1/(n/2)) = n/4 + 1/2 = **O(n)** 이 된다.

- 최소로 사용하는 방법 구하기

  24개가 있을 경우 절반씩 나눠서 비교한다면 4번만에 찾을 수 있다.

  반으로 나웠을 경우 홀수라면 2개를 비교하면 된다. (2개의 무개가 같으면 비교안한 한개가 가짜 동전이 있다.)

  동전의 개수가 n 이 된다면

  - 2개 => 1번 , 3개 => 1번, 4개 => 2번, 5개 => 2번, 6개 => 2번, 7개 => 2번, 8개 => 3번

    8개일 경우 3, 3, 2로 나누면 2번으로 줄어드나 상수값의 차이기에 O() 표기법에 영향 X 기에 고려하지 않는다.

  - 2^k <= n < 2^(k+1) n개의 동전일 경우 k 번 즉 **logn** 번만에 찾아낼 수 있다.

- O(n) vs O(logn) 의 경우 n 이 커질 때 O(n)도 커지지만 O(logn)은 상대적으로 일정시간이내에 해결할 수 있다. 즉 빠르다.

#### 분할 정복 기법

- 설계 전략
  - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine) : (필요하다면) 해결된 해답을 모은다.

- Top-down Approach (하향식 접근법)

  원래 문제를 해결하기 위해서 작은 부분부터 해결한다.

#### 거듭제곱

##### 반복(Iterative) 알고리즘 : O(n)

- C의 거듭제곱 = 1에 거듭제곱할 값만큼 C를 곱하는 방식으로 연산 수행

  ```python
  def interative_power(C, n):
      result = 1
      for _ in range(n): # 총 n 번의 곱셈을 수행 => O(n)
          result = result + C
      return result
  ```

##### 분할 정복 기반 알고리즘 : O(logn)

- 거듭제곱을 반씩 나누어서 곱해 나가는 방식으로 풀이

  - ex-even) C^8 = C * C * C * C* C * C * C * C = C^4 * C^4 = (C^4)^2
  - ex-odd) C^9 = C^4 * C^4 *C

- 지수가 1이 되면 밑 수를 그대로 반환 => 시간 복잡도를 O(logn)으로 줄일 수 있음

  ```python
  def recursive_poser(C, n):
      if n == 1:
          return C
      if n % 2 == 0: # even
          y = recursive_power(C, n/2)
          return y * y
      else: # odd
          y = recursive_power(C, n/2)
          return y * y * C
  ```

#### 병합 정렬 (Merge Sort)

- **여러 개의 정렬된 자료**의 집합을 병합하여 **한 개의 정렬된 집합**으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 **나눈 후**에 차례대로 **정렬**하여 최종 결과를 얻어냄
  - top-down 방식

- 시간 복잡도 : O(nlogn)

##### 병합 정렬 과정

1. 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
2. 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합한다.
   - 각 단계마다 n번 순회 나눠지는 단계는 logn 이기에 nlogn 이된다.
   - 시간 복잡도 O(nlogn)

##### 알고리즘

```python
# 분할 함수
def merge_sort(arr):
    # 절반으로 나누어서 각각을 해결하는 부분
    if len(arr) == 1:
        return arr
    # 절반으로 나누어서 각각 별도의 정렬 실행
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 각 나눈 문제를 해결
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)  # => 통합

# 병합 함수 1
def merge(arr1, arr2):
    # 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
    result = []
    # 병합 과정 실행
    # 각각의 최소값들(가장 앞쪽 값)을 비교해서 더 작은 요소를 결과에 추가
    # 두 부분집합에 요소가 없어질 때까지 계속 반복
    while arr1 or arr2:
        if arr1 and arr2:
            # 두 부분집합의 요소가 모두 남아 있을 경우
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif arr1:
            result.append(arr1.pop(0))
        elif arr2:
            result.append(arr2.pop(0))
    return result


arr = [6, 2, 4, 1, 7, 8, 9, 3]
print(merge_sort(arr)) # [1, 2, 3, 4, 6, 7, 8, 9]
```

```python
# 인덱스 이용한 병합 함수 2
def merge2(arr1, arr2):
    result = []
    i = j = 0  # index
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        elif j < len(arr2):
            result.append(arr2[j])
            j += 1
    return result
```



### 백트래킹

### 트리