# SW Expert D2

```python
# 1989. 초심자의 회문 검사

tc = int(input())

for i in range(1, tc+1):
    # 입력
    word = input()
    result = 0
    # 계산
    if word == word[::-1]:
        result = 1
    else:
        result = 0

    # 출력
    print('#{} {}'.format(i, result))
```

```python
# 2369. [AtCoder Beginner Contest 073] B. Theater

tc = int(input())

for i in range(tc):
    row = int(input())
    result = 0
    for r in range(row):
        seat1, seat2 = map(int, input().split())
        result += seat2 - seat1 + 1

    print('#{} {}'.format(i+1, result))
```

```python
# 2357. [AtCoder Beginner Contest 073] A. September 9 

tc = int(input())

for i in range(tc):
    num = input()
    for n in num:
        if n == '9':
            result = 'Yes'
            break
    else:
        result = 'No'

    print('#{} {}'.format(i+1, result))
```

```python
# 1945. 간단한 소인수분해

tc = int(input())
for t in range(tc):
    num = int(input())
    factor = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]

    for i in range(5):
        count = 0
        while True:
            if num % factor[i] == 0:
                count += 1
                num = num//factor[i]
            else:
                result[i] = count
                break
    print('#{} '.format(t+1),end='')
    for j in range(5):
        print('{}'.format(result[j]),end=' ')
    print()
```

```python
# 1986. 지그재그 숫자

tc = int(input())
for t in range(tc):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i%2:
            result += i
        else:
            result -= i

    print('#{} {}'.format(t+1,result))
```

```python
# 1926. 간단한 369게임

N = int(input())
N_str = ''
for n in range(1, N+1):
    N_str += str(n) + ' '


N_str = N_str.replace('3','-')
N_str = N_str.replace('6','-')
N_str = N_str.replace('9','-')
for i in range(1, 10):
    b = str(i)+'-'
    N_str = N_str.replace(b, '-')
for i in range(10):
    a = '-'+str(i)
    N_str = N_str.replace(a, '-')
print(N_str)
```

```python
# 2001. 파리 퇴치

tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    fly = [[0 for _ in range(N)] for _ in range(N)]
    fkill = 0
    for i in range(N):
        fly[i] = list(map(int, input().split()))

    for a in range(N-M+1):
        for b in range(N-M+1):
            kill = 0
            for m1 in range(M):
                for m2 in range(M):
                    kill += fly[a+m1][b+m2]
                    if fkill < kill:
                        fkill = kill



    print('#{} {}'.format(t+1,fkill))
```

```python
# 1984. 중간 평균값 구하기

tc = int(input())
for t in range(tc):
    num = list(map(int, input().split()))
    num.sort()
    num.pop(0)
    num.pop(-1)
    result = sum(num)/len(num)
    result = int(round(result, 0))


    print('#{} {}'.format(t+1,result))
```

```python
# 1983. 조교의 성적 매기기

tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    K -= 1
    student_lst = [[0 for _ in range(3)] for _ in range(N)]
    score_lst = [0]*N
    clscore_lst = [0]*N

    grade = ['A+', 'A0', 'A-','B+', 'B0', 'B-','C+', 'C0', 'C-','D0']
    for i in range(N):
        student_lst[i] = list(map(int, input().split()))
        score_lst[i] = round(student_lst[i][0]* 0.35 + student_lst[i][1]* 0.45 + student_lst[i][2]* 0.20, 2)
    clscore_lst = list(score_lst)
    clscore_lst.sort(reverse=True)
    gradeidx = clscore_lst.index(score_lst[K])//(N//10)

    print('#{} {}'.format(t+1,grade[gradeidx]))
```

```python
# 1966. 숫자를 정렬하자

tc = int(input())
for t in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    result =''
    for i in range(len(lst)):
        result += str(lst[i]) + ' '

    print('#{} {}'.format(t+1,result))
```

```python
# 2007. 패턴 마디의 길이

testcase = int(input())

for tc in range(testcase):
    sentence = input()
    print(sentence)
    for i in range(1, 10):
        if sentence[0:i] == sentence[i:i+i]:
            result = i
            break

    print('#{} {}'.format(tc+1, result))
```

```python
# 2005. 파스칼의 삼각형

testcase = int(input())

for tc in range(testcase):
    N = int(input())
    pascal = [[1] for _ in range(N)]
    for i in range(1, N):
        pascal[i] = [1] * (i+1)

    if N > 2:
        for i in range(2, N):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    print('#{}'.format(tc+1))

    for i in range(N):
        for j in range(i+1):
            print(pascal[i][j],end=' ')
        print()
```

```python
# 1976. 시각 덧셈

testcase = int(input())

for tc in range(testcase):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2

    while m > 60:
        h += 1
        m -= 60
    while h > 12:
        h -= 12

    print('#{} {} {}'.format(tc+1, h, m))

```

```python
# 1979. 어디에 단어가 들어갈 수 있을까

## sol 1
testcase = int(input())

for tc in range(testcase):
    N, K = map(int, input().split())

    puzzlelst = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        puzzlelst[i] = list(map(int, input().split()))
    finalcount = 0

    # 가로탐색
    for x in range(N):
        count = 0
        for y in range(N):
            if puzzlelst[x][y] == 1:
                count += 1
                if y == N-1 and count == K:
                    finalcount += 1
                elif y != N-1 and puzzlelst[x][y+1] == 0 and count == K:
                    finalcount += 1
            else:
                count = 0


    # 세로 탐색
    for y in range(N):
        count = 0
        for x in range(N):
            if puzzlelst[x][y] == 1:
                count += 1
                if x == N-1 and count == K:
                    finalcount += 1
                elif x != N-1 and puzzlelst[x+1][y] == 0 and count == K:
                    finalcount += 1
            else:
                count = 0

    print('#{} {}'.format(tc+1, finalcount))
 
## sol 2
T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 가로 확인
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                temp += 1
                if j < N-1 and puzzle[i][j+1] == 0 and temp==K:
                    result += 1
                elif j == N-1 and temp == K:
                    result += 1
            else:
                temp = 0

    # 세로 확인
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                temp += 1
                if j < N-1 and puzzle[j+1][i] == 0 and temp==K:
                    result += 1
                elif j == N-1 and temp == K:
                    result += 1
            else:
                temp = 0


    print('#{} {}'.format(tc+1, result))
```

```python
# 1970. 쉬운 거스름돈

testcase = int(input())

for tc in range(testcase):
    money = int(input())
    price = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*8

    for i in range(8):
        while money >= price[i]:
            result[i] += 1
            money = money - price[i]

    print('#{}'.format(tc+1))
    for i in range(8):
        print('{}'.format(result[i]), end=' ')
    print()

```

```python
# 1946. 간단한 압축 풀기

testcase = int(input())

for tc in range(testcase):
    N = int(input())
    file = ''
    print('#{}'.format(tc + 1))
    for i in range(N):
        text, num = map(str, input().split())
        num = int(num)
        for i in range(num):
            file += text
            if len(file) == 10:
                print(file)
                file = ''

    print(file)
```

```python
# 1974. 스도쿠 검증

T = int(input())

for tc in range(T):
    Sudoku = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        row_check = []
        col_check = []
        for j in range(9):
            row_check.append(Sudoku[i][j])
            col_check.append(Sudoku[j][i])
        if len(set(row_check)) == 9 and len(set(col_check)) == 9:
            result = 1
        else:
            result = 0
            break


    if result == 1:
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                square_check = []
                for i in range(3):
                    for j in range(3):
                        square_check.append(Sudoku[x+i][y+j])
                if len(set(square_check)) != 9:
                    result = 0
                    break

    print('#{} {}'.format(tc+1, result))
```

```python
# 1961. 숫자 배열 회전

## sol 1
def rotation(lst, N): # 90도 회전
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = lst[N-j-1][i]
    return result

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    lst1 = rotation(numbers, N)
    lst2 = rotation(lst1, N)
    lst3 = rotation(lst2, N)

    print('#{}'.format(tc+1))

    for i in range(N):
        result = ''
        for j in range(N):
            result += str(lst1[i][j])
        result += ' '
        for j in range(N):
            result += str(lst2[i][j])
        result += ' '
        for j in range(N):
            result += str(lst3[i][j])

        print(result)
        
## sol 2
testcase = int(input())

def rotate(lst,N):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = lst[N-j-1][i]
    return result

for tc in range(testcase):
    N = int(input())
    lst = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        lst[i] = list(map(int, input().split()))

    lst_1 = rotate(lst, N)
    lst_2 = rotate(lst_1, N)
    lst_3 = rotate(lst_2, N)

    for i in range(N):
        for j in range(N):
            lst_1[i][j] = str(lst_1[i][j])
            lst_2[i][j] = str(lst_2[i][j])
            lst_3[i][j] = str(lst_3[i][j])


    print('#{}'.format(tc+1))

    for i in range(N):
        print(''.join(lst_1[i]),end=' ')
        print(''.join(lst_2[i]),end=' ')
        print(''.join(lst_3[i]),end=' ')
        print()
```

```python
# 1948. 날짜 계산기

T = int(input())

for tc in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    monthday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 0

    for i in  range(m1, m2+1):
        if i == m1:
            day += monthday[m1] - d1 + 1
        elif i == m2:
            day += d2
        else:
            day += monthday[i]

    print('#{} {}'.format(tc+1, day))
```

```python
# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())

for tc in range(T):
    tc_num = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    manyvalue = 0
    for i in range(1, 101):
        if cnt <= numbers.count(i):
            cnt = numbers.count(i)
            manyvalue = i

    print('#{} {}'.format(tc_num, manyvalue))

```

```python
# 1285. 아름이의 돌 던지기

T = int(input())

for tc in range(T):
    people = int(input())
    stone = list(map(int, input().split()))

    distance = 100000
    num_people = 0

    # 0 과 가까운 거리 찾기
    for i in range(people):
        if abs(stone[i]) < distance:
            distance = abs(stone[i])


    # 사람 수 찾기
    num_people += stone.count(distance) + stone.count(-distance)


    print('#{} {} {}'.format(tc+1, distance, num_people))
```

```python
# 1954. 달팽이 숫자

def move(x, y, status, N):
    if status == 0:
        if y == N-1:
            status += 1
        elif board[x][y+1] != 0:
            status += 1
        else:
            status = 0
    elif status == 1:
        if x == N-1:
            status += 1
        elif board[x+1][y] != 0:
            status += 1
        else:
            status = 1
    elif status == 2:
        if y == 0:
            status += 1
        elif board[x][y-1] != 0:
            status += 1
        else:
            status = 2
    else:
        if x == 0:
            status = 0
        elif board[x-1][y] != 0:
            status = 0
        else:
            status = 3

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x += dx[status]
    y += dy[status]

    return x, y, status



T = int(input())

for tc in range(T):
    print('#{}'.format(tc+1))
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]

    x = y = 0
    direction = 0
    for i in range(1, N*N+1):
        board[x][y] = i
        x, y, direction = move(x, y, direction, N)

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
```

```python
# 1284. 수도 요금 경쟁

T = int(input())

for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    A_price = W * P
    if W <= R:

        B_price = Q
    else:
        B_price = Q + (W - R) * S

    final_price = min(A_price, B_price)

    print('#{} {}'.format(tc+1, final_price))
```

```python
# 1940. 가랏! RC카!

T = int(input())
for tc in range(T):
    test = int(input())
    car = 0
    distance = 0
    for i in range(test):
        selection = list(map(int, input().split()))
        if selection[0] == 1:
            car += selection[1]
            distance += car
        elif selection[0] == 2:
            car -= selection[1]
            if car < 0:
                car = 0
            else:
                distance += car
        else:
            distance += car

    print('#{} {}'.format(tc+1, distance))
```

```python
# 1288. 새로운 불면증 치료법

T = int(input())
for tc in range(T):
    N = input()
    numlst = [0]*10

    k = 0
    while numlst.count(0) != 0:
        k += 1
        Nk = str(int(N) * k)
        for i in Nk:
            numlst[int(i)] += 1

    print('#{} {}'.format(tc+1, Nk))
```
