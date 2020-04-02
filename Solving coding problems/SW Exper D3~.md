# SW Exper D3~

### 1959. 두 개의 숫자열

```python
for t in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    ans = -100000
    for i in range(M-N+1):
        sum = 0
        for j in range(N):
            sum += A[j]*B[i+j]
        if ans < sum:
            ans = sum

    print('#{} {}'.format(t+1, ans))
```

### 4047. 영준이의 카드 카운팅

```python
# my solution
for t in range(int(input())):
    card = input()
    cardlist = [0]*(len(card)//3)
    for i in range(len(card)//3):
        cardlist[i] = card[3*i:3*i+3]
    cardnums = [13, 13, 13, 13]
    ans = ''
    # print(cardlist)

    if len(set(cardlist)) != len(cardlist):
        ans = 'ERROR'

    else:
        for i in range(len(cardlist)):
            if cardlist[i][0] == 'S':
                cardnums[0] -= 1
            elif cardlist[i][0] == 'D':
                cardnums[1] -= 1
            elif cardlist[i][0] == 'H':
                cardnums[2] -= 1
            else:
                cardnums[3] -= 1

        for i in range(4):
            ans += str(cardnums[i]) + ' '

    print('#{} {}'.format(t+1, ans))
```

```python
# teacher solution
for tc in range(1, int(input()) + 1):
    arr = input()
    # 필요한 카드 개수
    cnt = [13] * 4

    # 개별 카드 정보를 식별, 3개씩 읽어오기
    cards = set()
    for i in range(0, len(arr), 3):  # 카드 시작 위치
        temp = arr[i: i + 3]  # 카드 중복 체크를 위해
        if temp in cards:
            cnt = 'ERROR'
            break  # ERROR
        cards.add(temp)
        if temp[0] == 'S':
            cnt[0] -= 1
        elif temp[0] == 'D':
            cnt[1] -= 1
        elif temp[0] == 'H':
            cnt[2] -= 1
        else:
            cnt[3] -= 1
    print(cnt)
```

### 2805. 농작물 수확하기

```python
for t in range(1, int(input()) + 1):
    N = int(input())
    crops = [list(map(int, input())) for _ in range(N)]
    ans = sum(crops[N//2])

    plus = N
    start = 0
    for i in range(N//2-1, -1, -1):
        plus -= 2
        start += 1
        for j in range(plus):
            ans += crops[i][start+j]
            ans += crops[N-i-1][start+j]

    print('#{} {}'.format(t, ans))
```

### 3347. 올림픽 종목 투표

```python
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    vote = [0] * N
    B = list(map(int, input().split()))

    for b in B:
        for i in range(N):
            if A[i] <= b:
                vote[i] += 1
                break
    print(vote)

    print('#{} {}'.format(t, vote.index(max(vote))+1))
```

### 4408. 자기 방으로 돌아가기

```python
for t in range(1, int(input()) + 1):
    N = int(input())
    rooms = [0] * 201
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        if start%2 == 0:
            start -= 1
        for i in range(start, end+1, 2):
            rooms[int(i/2)] += 1

    print('#{} {}'.format(t, max(rooms)))
```

### 6190. 정곤이의 단조 증가하는 수

```python
for t in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    lst = []

    for i in range(N):
        for j in range(i+1, N):
            num = str(A[i]*A[j])
            for k in range(len(num)-1):
                if int(num[k]) > int(num[k+1]):
                    break
            else:
                lst.append(int(num))
    lst.sort()

    if len(lst) == 0:
        result = -1
    else:
        result = lst[-1]
    print('#{} {}'.format(t, result))
```

### 1974. 스도쿠 검증

```python
for t in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):

        row = [0] * 10
        col = [0] * 10
        for j in range(9):
           if row[arr[i][j]] == 1 or col[arr[j][i]] == 1:
               ans = 0
               break
           row[arr[i][j]] = 1
           col[arr[j][i]] = 1

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            c = [0] * 10
            for i in range(3):
                for j in range(3):
                    if c[arr[i+x][j+y]] == 1:
                        ans = 0
                        break
                    c[arr[i+x][y+j]] = 1


    print('#{} {}'.format(t+1,ans))
```

### 3349. 최솟값으로 이동하기

```python
for t in range(int(input())):
    W, H, N = map(int, input().split())
    cnt = 0
    x, y = map(int, input().split())
    for i in range(N-1):
        xn, yn = map(int, input().split())
        dx = x - xn
        dy = y - yn
        if dy*dx > 0:
            cnt += max(abs(dx), abs(dy))
        else:
            cnt += abs(dx) + abs(dy)
        x, y = xn, yn

    print('#{} {}'.format(t+1, cnt))
```

### 2001. 파리 퇴치

```python
for t in range(int(input())):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for k in range(M):
                for k2 in range(M):
                    catch += fly[i+k][j+k2]
            ans = max(catch, ans)
            
    print('#{} {}'.format(t+1, ans))
```

### 5356. 의석이의 세로로 말해요

```python
for t in range(int(input())):
    arr = [['-1']*15 for _ in range(5)]
    ans = ''
    for i in range(5):
        inputV = input()
        for j in range(len(inputV)):
            arr[i][j] = inputV[j]
    for j in range(15):
        for i in range(5):
            if arr[i][j] == '-1':
                pass
            else:
                ans += arr[i][j]
    print('#{} {}'.format(t+1, ans))
```

### 4613. 러시아 국기 같은 깃발

```python
# teacher solution 1
for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = N*M
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            cnt = 0
            for r in range(0, i+1):
                for c in range(M):
                    if arr[r][c] != 'W': cnt += 1
            for r in range(i+1, j+1):
                for c in range(M):
                    if arr[r][c] != 'B': cnt += 1

            for r in range(j+1, N):
                for c in range(M):
                    if arr[r][c] != 'R': cnt += 1
            ans = min(ans, cnt)
    print('#{} {}'.format(t+1,ans))
```

```python
# teacher solution 2 - 누적합 이용
for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    w = [0] * N
    b = [0] * N
    r = [0] * N
    for i in range(N):
        w[i] = arr[i].count('W')
        b[i] = arr[i].count('B')
        r[i] = M - w[i] - b[i]

    for i in range(1, N):
        w[i] += w[i - 1]
        b[i] += b[i - 1]
        r[i] += r[i - 1]

    ans = N * M
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            # 전체 칸 수 에서 바꿀 필요 없는 칸수 빼서 구하기
            cnt = M * (i+1) - w[i]
            cnt += M * (N - 1 - (j+1) + 1) - (r[N-1] - r[j])

            ans = min(ans, cnt)
    print('#{} {}'.format(t+1,ans))
```



![image-20200313163453000](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200313163453000.png)



![image-20200313163809849](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200313163809849.png)



![image-20200313164201852](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200313164201852.png)