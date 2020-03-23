# 백준 A형 대비 문제

> https://www.acmicpc.net/

```python
# 14499번 주사위 굴리기

def dir1(x, y, move, N, M):
    d = [[0,0], [0, 1], [0, -1], [-1, 0], [1, 0]]
    x += d[move][0]
    y += d[move][1]
    if 0 <= x < N and 0 <= y < M:
        decide = True
    else:
        decide = False
        x -= d[move][0]
        y -= d[move][1]
    return x, y, decide

def dir2(dice, move):
    if move == 4: # 남
        temp = dice[0]
        for i in range(4):
            dice[i] = dice[i + 1]
        dice[3] = temp
    elif move == 3: # 북
        temp = dice[3]
        for i in range(3, -1, -1):
            dice[i] = dice[i - 1]
        dice[0] = temp
    elif move == 1: # 동
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = dice[4]
        dice[4] = temp
    else: # 서
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = dice[5]
        dice[5] = temp
    return dice

N, M, x, y, move_num = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]

move = input().split()
for i in range(len(move)):
    move[i] = int(move[i])

dice = [0] * 6

dice[1] = map[x][y]
for i in range(move_num):
    x, y, decide = dir1(x, y, move[i], N, M)
    if decide:
        dice = dir2(dice, move[i])
        if map[x][y] == 0:
            map[x][y] = dice[1]
        else:
            dice[1] = map[x][y]
            map[x][y] = 0


        print(dice[3])
```

```python
# 14502번 연구소
```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```









