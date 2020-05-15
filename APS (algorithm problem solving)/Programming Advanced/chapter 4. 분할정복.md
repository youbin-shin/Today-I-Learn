# chapter 4. 분할정복

2020.05.04

> 학습목표
>
> - 문제를 분할해서 핵5ㅕㄹ하는 분할 정복 (Divide and Conquer) 기법을 이해하고 대표적인 알고리즘인 퀵 정렬과 병합 정렬에 대해 학습한다.
> - 상태 공간 트리의 모든 노드를 검색하는 백트래킹에 대해 학습한다.
> - 이진 트리(Binary Tree)의 특성을 이애하고 이진 트리의 중요한 연산인 탐색, 삽입, 삭제 알고리즘을 학습한다.

## 분할정복

### 문제 제시 : 가짜 동전 찾기

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

### 분할 정복 기법

- 설계 전략
  - 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
  - 통합(Combine) : (필요하다면) 해결된 해답을 모은다.

- Top-down Approach (하향식 접근법)

  원래 문제를 해결하기 위해서 작은 부분부터 해결한다.

### 거듭제곱

#### 반복(Iterative) 알고리즘 : O(n)

- C의 거듭제곱 = 1에 거듭제곱할 값만큼 C를 곱하는 방식으로 연산 수행

  ```python
  def interative_power(C, n):
      result = 1
      for _ in range(n): # 총 n 번의 곱셈을 수행 => O(n)
          result = result + C
      return result
  ```

#### 분할 정복 기반 알고리즘 : O(logn)

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

### 병합 정렬 (Merge Sort)

- **여러 개의 정렬된 자료**의 집합을 병합하여 **한 개의 정렬된 집합**으로 만드는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위의 문제까지 **나눈 후**에 차례대로 **정렬**하여 최종 결과를 얻어냄
  - top-down 방식

- 시간 복잡도 : O(nlogn)

#### 병합 정렬 과정

1. 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
2. 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합한다.
   - 각 단계마다 n번 순회 나눠지는 단계는 logn 이기에 nlogn 이된다.
   - 시간 복잡도 O(nlogn)

#### 알고리즘

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

### 퀵 정렬 (Quick Sort)

- 주어진 배열을 두 개로 분할하고 각각 정렬한다.

  - 병합 정렬과 차이점
    1. 병합 정렬은 그냥 두 부분으로 나누는 반몀ㄴ, 퀵 정렬은 분할할 때, 기준 아이템(`pivot item`) 중심으로, 이보자 작은 것은 왼쪽, 큰것은 오른쪽에 위치시킨다.
    2. 각 부분 정렬이 끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하나 퀵 정렬은 필요하지 않는다.

- 시간복잡도는 평균적으로 O(nlogb)이다.

  최악의 경우 병합정렬 O(nlogn)보다 O(n^2)로 더 오래걸릴 수 있다.

#### 1. Hoare-partition 알고리즘

`pivot` 위치 결정

```python
def hoare_partition(arr, left, right):
    # i, j를 설정하고, 큰값 찾고, 작은값 찾아서 위치 바꿔주기
    i = left
    j = right
    pivot = arr[left] # pivot 리스트 처음값을 기준으로 함
    
    # i가 j보다 작을 때까지 계속해서 반복
    while i <= j: # 교차될 때 그 지점이 pivot
        # pivot 보다 큰값이 나올 때까지 i 증가
        while i <= j and arr[i] <= pivot:
            i += 1
        # pivot 보다 작은값이 나올 때까지 j 증가
        while i <= j and arr[j] >= pivot:
            j -= 1
        # i가 j 보다 작으면, 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left] # pivot 위치 결정
    
    return j  # pivot 위치 = j
```

- pivot 선택 : 왼쪽 선택, 오른쪽 끝, 임의의 세 개 값 중에 중간 값
- pivot 위치 잡기 : i와 j 가 교차하면, i, j는 pivot을 기준으로 작은 값과 큰 값들의 경계에 위치한다.

#### 2. Lomuto-partition 알고리즘

Hoare-partition 보다 교환이 더 일어난다.

```python
def lomuto_partition(arr, left, right):
    # 맨 오른족 요소를 pivot으로 설정
    # i = left - 1, j = 0
    pivot = arr[right]
    i = left - 1
    j = left
    
    for i in range(left, right):
        # arr[i] 가 pivot보다 작으면,
        if arr[j] < pivot:
            #  i를 1 증가
            # arr[j], arr[i] 위치 교환
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # i가 가르키는 위치가 pivot보다 작은 값의 마지막 인덱스
    # i + 1의 위치에 pivot을 두고 i + 1을 반환
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1
```

#### 퀵 정렬 알고리즘

Hoare-partition 알고리즘 이용 예시

```python
def quick_sort(arr, left, right): # 왼쪽 시작점, 오른쪽 끝지점 지정
    # pivot 위치 결정 (pivot을 기준으로 큰값은 오른쪽, 작은값은 왼쪽으로 구분)
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left < right:
        # pivot 구하기
        pivot = hoare_partition(arr, left, right)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        #오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)

def hoare_partition(arr, left, right):
    # i, j를 설정하고, 큰값 찾고, 작은값 찾아서 위치 바꿔주기
    i = left
    j = right
    pivot = arr[left]
    
    # i가 j보다 작을 때까지 계속해서 반복
    while i <= j:
        # pivot 보다 큰값이 나올 때까지 i 증가
        while i <= j and arr[i] <= pivot:
            i += 1
        # pivot 보다 작은값이 나올 때까지 j 증가
        while i <= j and arr[j] >= pivot:
            j -= 1
        # i가 j 보다 작으면, 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left] # pivot 위치 결정
    
    return j
    
    
arr = [4, 5, 1, 2, 7, 9, 8, 3]
quick_sort(arr, 0, len(arr)-1)
print(arr) # [1, 2, 3, 4, 5, 7, 8, 9]
```

![image-20200514151715276](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200514151715276.png)

### 이진 검색 (Binary Search)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 이진 검색을 하기 위해서는 **자료가 정렬된 상태**여야 한다.

#### 검색 과정

1. 자료의 중앙에 있는 원소를 고른다. `중앙인덱스 = (left + right) // 2`
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

#### 알고리즘

```python
# 반복 구조

def binarySearch(n, lst, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```

```python
# 재귀 구조

def binarySearch(lst, low, high, key):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if key = lst[mid]:
            return mid
        elif key < lst[mid]:
            return binarySearch(lst, low, mid-1, key)
        else:
            return binarySearch(lst, mid + 1, high, key)
```

#### 문제 제시 : 병뚜껑 속 숫자 게임

- 술레가 병뚜껑 속 숫자를 확인한 후 다음 사람부터 숫자를 맞히기 시작한다. 술래는 up 또는 down 을 통해 게임에 참여한 사람들이 병뚜껑 속 숫자에 점점 가까워질 수 있도록 힌트를 제시한다.
- 이 게임은 숫자를 맞히는 게 아니라 피하는게 핵심! 최대한 빨리 당첨되려면 어떻게 하면 될까요?


