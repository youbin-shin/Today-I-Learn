# Intermediate 예제 기지국 문제

SS 텔레콤에서 현재 기지국의 위치와 집들이 표시된 지도를 2차원 nxn 배열로 변환하여, 기지국에 커버 되지 않는 집의 수를 찾고자 한다. 기지국은 [그림1]과 같이 세가지 종류가 있다. 각각의 기지국은 기지국이 위치한 셀에서 동서남북으로 각 1개, 2개, 3개의 셀을 커버하며, 하나의 집은 1개의 셀에 있다. 

[문제] 주어진 2차원 배열 지도에 위치한 기지국으로 커버되지 않는 집의 수를 찾는 프로그램을 작성하시오. [제약사항] 2차원 배열의 크기의 n은 50이하이다. 기지국의 수는 50이하이다

[입력] 첫 줄에는 테스트 케이스의 수가 주어지고, 그 다음 줄부터 각 테스트 케이스가 n+1개의 줄로 구성된 다. 테스트 케이스의 첫 줄에는 n이 주어지고, 다음 n개 줄에는 2차원 배열의 각 행이 한 줄에 차례로 주어진다. 단, 집이 위치한 원소는 ‘H’, 기지국이 위치한 원소는 ‘A’, ‘B’, ‘C’로 표시하며, 각각 동서남북 으로 1, 2, 3개를 커버하는 기지국이다. ‘X’인 원소는 아무 것도 없다는 것을 나타낸다. 

```python
T = int(input())

for t in range(T):
    N = int(input())
    town = [list(input()) for _ in range(N)]
    A = []
    B = []
    C = []

    for i in range(N):
        for j in range(N):
            if town[i][j] == 'A':
                A.append([i,j])

            if town[i][j] == 'B':
                B.append([i,j])

            if town[i][j] == 'C':
                C.append([i,j])

    for i in range(len(A)):
        x = A[i][0]
        y = A[i][1]
        for j in range(-1, 2, 2):
            X = x + j
            Y = y + j
            if 0 <= X < N and 0 <= Y < N:
                if town[X][y] == 'H':
                    town[X][y] = 'X'
                if town[x][Y] == 'H':
                    town[x][Y] = 'X'


    for i in range(len(B)):
        x = B[i][0]
        y = B[i][1]
        for j in range(-2, 3):
            X = x + j
            Y = y + j
            if 0 <= X < N and 0 <= Y < N:
                if town[X][y] == 'H':
                    town[X][y] = 'X'
                if town[x][Y] == 'H':
                    town[x][Y] = 'X'


    for i in range(len(C)):
        x = C[i][0]
        y = C[i][1]
        for j in range(-3, 4):
            X = x + j
            Y = y + j
            if 0 <= X < N and 0 <= Y < N:
                if town[X][y] == 'H':
                    town[X][y] = 'X'
                if town[x][Y] == 'H':
                    town[x][Y] = 'X'

    cnt = 0
    for x in range(N):
        for y in range(N):
            if town[x][y] == 'H':
                cnt += 1

    print('#{} {}'.format(t+1, cnt))
```

```python
## input

5
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
9
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXBHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX
9
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XHHXXXXXX
XXXHHXXXX
XXHHCHXHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX
10
XXXXXXXXXX
XXXXHXXXXX
XXHAHXXHXX
xXXHHXXXXX
XXHXXXXXXX
XXBHHXXXXX
XXHXXXHAHX
XXAHXXXHXX
XXHXXHXXXX
XXXXXBXXXX
20
XXXXXXHXXXXXXHXHXXXX
XXXHXXHXXXXXHAHXXHXX
XXHAHXXCHXXXXXHHXXXX
XXHHXXXHXXXXHBHHXXXX
XHHXXXXHXXXXHHHCHXHX
XXXHHXXXXXXXHXXHXXXX
XXHHCHXHXXXXHAHXXHXX
XXAHXXHXXXBXXHHXXXXX
XXHXHXXXXXHXXXHXXXXX
XXXXXXXXXXXXXHHCHXHX
XXXHXXXXXXXHXXHXXXXX
XXHAHXXHXXXXXHXXXXXX
XXHHXXXXXXXXAHXXXXXX
XXXXXXXXXXHXBHHXXXXX
XXAHHXXXXXHXBHXHXXXX
XXHXXHAHXXXXHXAHXXXX
XXAHXXHXXXXXHXXHXXXX
XXXXXXHXXXXXHXXHXXXX
XXHXHXXXXXXXHAHXXHXX
XXXXXXHXXXXXXHXHXXXX

```

```python
## output

#1 4
#2 2
#3 6
#4 3
#5 30
```

