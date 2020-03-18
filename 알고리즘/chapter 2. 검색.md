# chapter 2. 검색

> 2020.02.04 알고리즘_3

### 검색의 종류

#### 순차 검색

가장 직관적, 순서대로 자료 검색, 비효율적

```python
# a: 집합, n: 집합 개수, key: 확인하고 싶은 값
# a 정렬 X
def seqeuntialSearch(a, n, key):
    i = 0
    while i<n and a[i]!=key:
        i += 1
    if i < n : return 1
    else: return -1
```

```python
# a 정렬 O
def seqeuntialSearch2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key: return 1
    else: return -1
```

#### 이진 검색

전제 조건: 자료가 정리되어 있어야 함.

☆ 중앙 원소 값과 찾으려는 값과 비교

```python
# solution 1
def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

a = [2, 4, 6, 8, 9, 11]
print(binarySearch(a, 11)) # True
```

```python
# solution 2
# 재귀 함수 이용
def binarySearch(a, start, end, key):
    if start > end:
        return False
    else:
        middle = (start + end)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, start, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, end, key)
```

#### 해쉬

##### 셀렉션 알고리즘

자료에서 k번째로 크/작은 원소 찾는 알고리즘

```python
# k번째로 작은 원소를 찾는 알고리즘

def select(list, k):
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
		list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]
```

##### 선택 정렬 알고리즘

가장 작은 값의 원소부터 차례대로 선택하여 위치를 교화하는 방식

- 방법 

  리스트 중 최소값을 찾아 앞에 위치시킨다.
  
  이후 맨 처음 위치를 제외한 나머지 리스트에서 반복 실행

```python
def SelectionSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min],a[i]
    return a

a = [8, 4, 1, 9, 5]
print(SelectionSort(a))
```

### 연습 문제

|      |  dx  |  dy  |
| :--: | :--: | :--: |
|  →   |  0   |  1   |
|  ↓   |  1   |  0   |
|  ←   |  0   |  -1  |
|  ↑   |  -1  |  0   |

```python
# 이웃한 원소들의 합을 구하라
'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# 정답 : 24
def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5: return True
    return False

def calAbs(y, x):
    if y - x > 0: return y - x
    else: return x- y


arr = [[0 for x in range(5)] for x in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[x][y], arr[testX][testY])

print(f'sum = {}'.format(sum)) # 45
```

```python
# 달팽이 문제
# ary의 값을 크기순으로 데이터를 받아 벽에 닿거나 숫자가 있을 경우 방향을 바꾸어 정렬한다.
ary = [ [ 9, 20, 2, 18, 11 ],
	[ 19, 1, 25, 3, 21 ],
	[ 8, 24, 10, 17, 7 ],
	[ 15, 4, 16, 5, 6 ],
	[ 12, 13, 22, 23, 14 ] ]

sorted_ary = [[0  for _ in range(5)] for _ in range(5)]

def sel_min():
    minX, minY= 0, 0
    for i in range(5):
        for j in range(5):
            if ary[minX][minY] > ary[i][j]:
                minX, minY = i, j

    min = ary[minX][minY]
    ary[minX][minY] = 99
    return min

def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5: return True
    if sorted_ary[x][y] != 0: return True
    return False


X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_stat = 0  # 0:오른쪽, 1:아래, 2:왼쪽, 3:위

for i in range(25):
    cur_min = sel_min()
    sorted_ary[X][Y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]

    if isWall(X, Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]


for i in range(5):
    for j in range(5):
        print(sorted_ary[i][j], end=" ")
    print()
```
