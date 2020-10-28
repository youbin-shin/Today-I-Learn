# chapter 1. 배열 1

> 2020.01.30 알고리즘_1

### 알고리즘

유한한 단계를 통해 **문제를 해결하기 위한 절차나 방법**

- 시작과 끝 반드시 존재!

- 표현 방법 크게 2가지

  - 슈더코드 ( pseudo code ) 

    문법이 따로 존재 X

    대부분의 알고리즘에서 선호하는 표현방법

  - 순서도

    그림

- 좋은 알고리즘 기준 : 정확성, 작업량, 최적성 ★

- 시간 복잡도 - 성능 기준

  - 빅-오 (O) 표기법 ☆

    일반적

    연산의 수를 계산 > 계수와 상수 제거, 최고차항만 남김

    O(logn) 이때 밑은 숫자 2

    O(1) O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)

  - 세타 표기법

    논문에서 주로 사용

  - 오메가 표기법

- 주요 해결 방법

  1. 완전 검색 _ 모든 경우 탐색

  2. 그리디 
  3. 알고리즘분할 
  4. 정보다이나믹 프로그래밍 ( 동적 프로그래밍 )

---

### 배열

- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조 

- 자료형 ( Data types )

  - 정수형 ( integer, long )
  - 실수형 ( float, double )
  - 문자 ( char )

  **procedual language** - BASIC, C, PASCAL, FORTRAN

  **object-oriented language** - python, Java

  : procedual language 의기본자료형 + 객체 ( object ), 클라스 ( class )

- 필요성 : 하나의 선언으로 둘 이상의 변수 선언 가능

- *2차원 배열을 자유자재로 사용할 수 있으면 im 시험 통과*

- 2차원 배열

  num = [ [1,2], [3,4], [5,6] ] # 3행 2열

#### 연습문제 1 gravity

- 총 26개의 상자가 시계방향으로 90도 회전할 시 각 상자마다의 낙차가 가장 큰 결과를 리턴하여라.
- 해결방법
  1. 2차원 배열을 만들어서 상자가 있는 자리에는 1, 빈 공간에는 0을 배치한 뒤에 빈공간의 수 상자의 오른쪽 방향으로 0의 개수를 카운트해주어 구할 수 있다.
  2. 가장 낙차가 큰 값을 원하기에 상자의 꼭대기의 값만 구하면 된다.
  3. 상자 가장 높은 곳의 인데스만 가져와서 오른쪽방향으로 작은 값을 카운트해주면 된다.
  4. 2차원 배열을 연산하는 과정을 생략할 수 있다.
- 코드

```python
# my code
# input(각 상자의 높이 값) : 7 4 2 0 0 6 0 7 0


box = list(map(int, input().split()))
result = []

for i in range(len(box)):
    cnt = 0
    for j in range(i+1, len(box)):
        if box[i] > box[j]:
            cnt += 1
    result.append(cnt)

print(max(result))
```

```python
# teacher solution

arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
N = len(arr)

ans = 0
# 모든 꼭대기의 상자에 대해서 반복 수행
for i in range(N):
    # 상자 위치에서 바닥까지 거리
    h = N - 1 - i
    if ans >= h:
        break    
    # 자기 밑에 오는 상자의 수를 카운팅
    for j in range(i+1, N):
        if arr[i] <= arr[j]:
            h -= 1
    ans = max(ans, h)

print(ans)
```

#### 연습문제 2 baby-gin Game

- 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우면 run, 3장의 카드가 동일한 번호를 갖는 경우 triplet 이라 한다.

  6장의 카드가 run, triplet로만 구성될 경우 baby-gin으로 부른다.

  6자리 숫자를 입력 받아 baby-gin여부를 판단하는 프로그램을 작성하라.

- 코드

```python
# My code

# input
# 667767 -> baby-gin
# 054060 -> baby-gin
# 101123 -> x

for t in range(int(input())):
    card = [0] * 10
    mycard = input()
    
    for i in mycard:
        card[int(i)] += 1
        if card[int(i)] == 3:
            card[int(i)] = 0
    for i in range(8):
        sum = card[i] + card[i+1] + card[i+2]
        if sum == 3 or sum == 6:
            for j in range(3):
                card[i+j] -= 1

    if sum(card) == 0:
        print('babygin')
    else:
        print('fail')
```

#### 해결방안 알고리즘

1. 완전 검색

   순열을 이용하여 모든 경우를 나열한 후 3장, 3장씩 나눠서 run, triplet 다 확인하면 된다. 

   - 순열 만드는 방법 _ 간단, 무식_ 비추

     ```python
     # {1, 2, 3}으로 모든 순열 구하기
     for i1 in range(1, 4):
         for i2 in range(1, 4):
             if i2 != i1:
                 for i3 in range(1, 4):
                     if i3 != i1 and i3 != i2:
                         print(i1, i2, i3)
     ```

2. 탐욕 ( Greedy ) 알고리즘

   : 최적해를 구하는 데 사용되는 근시안적 방법

   : 최종적인 해답에 대한 증명 과정이 필요

   : *시험에 Greedy로 푸는 문제는 나오지 않는다. 검증된 Greedy 제외*

   - 동작 과정
     1. 해 선택
     2. 실행 가능성 검사
     3. 해 검사

   counts 배열에 run과 triplet 여부 판단하여 진행한다.

---

### 정렬

2개 이상의 자료를 특정 기준에 의해 오름차순/내림차순 재배열하는 것

- 대표적인 정렬

  - 버블 정렬

    기본적인 알고리즘, 인접한 데이터와 비교

    시간 복잡도: O(n^2) 

    ```python
    def BubbleSort(a):
        for i in range(len(a)-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j] # swap(a[i], a[i+1])
    ```

  - 카운팅 정렬

    데이터 중복이 많은 경우 사용

    데이터가 정수여야 정수로 표현할 수 있어야 사용가능

    시간 복잡도: O(n+k) # n: 리스트 길이, k: 정수의 최대값

    ```python
    def Counting_Sort(A, B, C):
    # A [1 .. n] 입력 배열
    # B = [0]*len(a) 정렬된 배열
    # C count list 카운트 배열
    
        C = [0] * k
    	
        # 카운트 리스트에 각 숫자 발생 빈도를 C 리스트에 저장
        for i in range(0, len(B)): 
            C[A[i]] += 1
    	
        # C 리스트에서 앞 인덱스 크기를 더해주기, 누적하여 인덱스 만들기 
        for i in range(1, len(C)):
            C[i] += C[i-1]
    
        for i in range(len(B)-1, -1, -1):
            B[C[A[i]]-1] = A[i]
            C[A[i]] -= 1
            
         return B
    

    a = [0, 4, 1, 3, 1, 2, 4, 1]
    b = [0] * len(a)
    k = max(a) + 1
    
    print(Counting_Sort(a, b, 5)) # [0, 1, 1, 1, 2, 3, 4, 4]
    ```
    



- 선택 정렬
  
- 퀵 정렬
  
- 삽입 정렬
  
- 병합 정렬
