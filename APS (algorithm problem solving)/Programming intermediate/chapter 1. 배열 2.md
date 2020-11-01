# chapter 1. 배열 2

> 2020.02.03 알고리즘_2

### 2차원 배열

```python
## N행의 2차원 배열
list(map(ist, input().split())) for _ in range(N)

# i 행 j 열
# 방법 1
for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j]

# 방법 2
for j in range(len(array[0])):
    for i in range(len(array)):
        array[i][j]
        
# 방법 3
for i in range(len(array)):
    for j in range(len(array[0])) :
        # 짝수행 - 순차적으로
        # 홀수행 - 역순으로
        array[i][j+(m-1-2*j)*(i%2)]
        
# 방법 4 - 델타 이용 ex
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]
[i,j] <= [i+dx,j+dy]
```

```python
# 전치행렬
for i in range( ):
    for j in range( ):
        if i < j:
        	arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

#### 연습문제 - dx, dy ★

**dx, dy 이용하는 것 능숙해지기**

5X5 2차 배열이 다음과 같이 있을 경우 이웃한 요소와의 차의 절대값을 더하는 값을 구하여라

1 1 1 1 1		25개의 요소에 대해 모두 조사하여 총합 구하기.

1 0 0 0 1		벽에 있는 요소는 이웃한 요소가 없음을 주의하기

1 0 0 0 1

1 0 0 0 1

1 1 1 1 1

```python
'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

def isWall(x,y):
    if x<0 or x>=5: return True
    if y<0 or y>=5: return True
    return False


def calAbs(y,x):
    if y-x > 0: return y-x
    else: return x-y

    
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
                
print(f'sum = {sum}')

# 출력값 sum = 24
```

---

### 비트 연산자

**2진수 연산**, 실행 속도 빠름, 실행 시간 효율적

#### & : and

```python
# & 이용하여 홀짝 구하기

num = int(input())
if num & 1:
    print('홀수입니다.')
else:
    print('짝수입니다.')
```

#### | : or

#### ^ : xor

값이 서로 다를 때 1 출력

```python
# XOR을 이용하여 0, 1 둘 중에 하나를 받을 때 반대로 출력하기

a = int(input()) # 0, 1
print(a^1)
```

#### >> : right shift

참고) 10진수의 경우 n*1/10배

#### <<n : left shift

참고) 10진수의 경우  n*10배

 2진수

 1101(13) << 1

 11010(26)

 << n 일경우 2**n만큼 곱해준 결과가 나온다.

##### 부분집합의 개수

1 << n : 2^n

원소가 n 개 일 경우의 모든 부분집합의 수를 의미한다.

ex)

i & (1 << j)

i = 5 = 101(2)

j = 0 , **1**, *2*

(1 << j) = 1, **10,** *100*

 i & (1 << j) = 101 & 1 = 1

​					**= 101 & 10 = 0**

​					*= 101 & 100 = 1*

=> 해당되는 위치의 값이 결과적으로 나온다.

```python
# 부분집합 구하기 ★

arr = [2, 3, 1]
n = len(arr)

for i in range(1<<n): # 1<<n = 8
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()

# 출력 : 2/ 3/ 2 3/ 1/ 2 1/ 3 1/ 2 3 1
```

```python
# 10개의 정수를 입력받아 부분집합의 합이 0이 되는 것이 존재하는지 계산하는 함수 구하기

arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# arr = list(map(int, input().split()))
sum = 0
cnt = 0

for i in range(1, 1 << len(arr)): # 1부터인 이유 : 공집합 제외
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
            sum += arr[j]
    if sum == 0:
        cnt += 1
        print("%d : " %cnt, end= " ")
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end= " ")
        print()
```
