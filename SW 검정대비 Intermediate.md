# SW 검정대비 Intermediate

>  https://www.acmicpc.net/problem/ 

2628 종이 자르기 2116 주사위 쌓기 2304 창고 다각형 2559 수열 2578 빙고 2477 참외밭 2527 직사각형 10157 자리배정 10158 개미 10163 색종이 13300 방 배정 14696 딱지놀이 2309 일곱 난장이 2605 줄 세우기 2563 색종이 2564 경비원 2491 수열

```python
# 2669  직사각형 네개의 합집합의 면적 구하기

plane = [[0 for _ in range(101)] for _ in range(101)]
for t in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2 - x1):
        for j in range(y2 - y1):
            if plane[x1 + i][y1 + j] == 0:
                plane[x1 + i][y1 + j] = 1

area = 0
for i in range(101):
    area += plane[i].count(1)

print(area)
```

```python
# 2635 수 이어가기

def seqence(f_num, s_num):
    result = [f_num, s_num]
    plus = f_num - s_num
    i = 2
    while plus >= 0:
        result.append(plus)
        plus = result[i-1] - result[i]
        i += 1

    return result


num = int(input())

max_cnt = 1
final_result = []

for n in range(num+1):
    result = seqence(num, n)
    # print(result)
    if max_cnt < len(result):
        max_cnt = len(result)
        final_result = result

print(max_cnt)


for i in range(max_cnt):
    print(final_result[i], end=' ')
```

```python
import sys
sys.stdin = open("input.txt","r")

switch_num = int(input())
switch_lst = [0] + list(map(int, input().split()))
st_num = int(input())

for i in range(st_num):
    student = list(map(int, input().split()))

    if student[0] == 1: # 남자
        status = student[1]

        for j in range(1, switch_num+1):
            if j % status == 0:
                if switch_lst[j] == 0:
                    switch_lst[j] = 1
                else:
                    switch_lst[j] = 0



    elif student[0] == 2:# 여자
        status = student[1]
        if switch_lst[status] == 0:
            switch_lst[status] = 1
        else:
            switch_lst[status] = 0

        for k in range(1, status):
            if 0 < k < switch_num and 0 < 2*status - k < switch_num:
                if switch_lst[k] == switch_lst[2*status - k]:
                    if switch_lst[k] == 1:
                        switch_lst[k] = 0
                        switch_lst[2 * status - k] = 0
                    else:
                        switch_lst[k] = 1
                        switch_lst[2 * status - k] = 1

for i in range(1, switch_num+1):
    print(switch_lst[i], end=' ')




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